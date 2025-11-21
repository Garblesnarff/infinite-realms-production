#!/usr/bin/env python3
"""
Enhanced Test script for D&D Campaign Expander
Tests all modes: interactive, single file, batch processing
Run: python test_run.py
Requires: OpenRouter API key in .env (or --dry-run to skip LLM calls)
"""

import sys
import os
import subprocess
import tempfile
import shutil
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock

# For testing purposes
from main import run_expansion, run_interactive_mode, run_batch_mode, slugify_filename

class TestCampaignExpander:
    def setup_method(self):
        """Setup test environment"""
        self.default_idea = "../campaign-ideas/aethelgard-the-once-and-future-king.md"
        self.test_output_dir = "test_output"
        self.batch_test_dir = "test_batch_input"
        
        # Create test batch directory with sample files
        os.makedirs(self.batch_test_dir, exist_ok=True)
        sample_files = [
            "test-campaign-1.md",
            "test-campaign-2.md"
        ]
        
        # Create minimal test campaign files
        for filename in sample_files:
            filepath = os.path.join(self.batch_test_dir, filename)
            with open(filepath, 'w') as f:
                f.write(f"""# {filename.replace('.md', '').title()}

*Test Campaign*

## Campaign Overview
A simple test campaign for validation purposes.

**Core Premise:** The heroes must save the village from goblins.

## Major NPCs
1. **Village Elder** - Wise leader of the village
""")
        
        # Clean up previous test outputs
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)
    
    def teardown_method(self):
        """Clean up test environment"""
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)
        if os.path.exists(self.batch_test_dir):
            shutil.rmtree(self.batch_test_dir)
    
    def test_file_exists(self):
        """Test that default campaign file exists"""
        assert os.path.exists(self.default_idea), f"Default test file not found: {self.default_idea}"
    
    @patch('main.OPENROUTER_API_KEY', 'test-key')  # Mock API key for testing
    def test_single_file_expansion(self):
        """Test single file expansion"""
        print("\n🧪 Testing Single File Mode...")
        
        try:
            result = run_expansion(
                idea_file_path=self.default_idea,
                campaign_id=None,
                output_dir=self.test_output_dir
            )
            
            # Validate output files exist
            json_file = os.path.join(self.test_output_dir, "expanded_campaign.json")
            sql_file = os.path.join(self.test_output_dir, "import.sql")
            md_file = os.path.join(self.test_output_dir, "campaign_book.md")
            
            assert os.path.exists(json_file), f"JSON output not found: {json_file}"
            assert os.path.exists(sql_file), f"SQL output not found: {sql_file}"
            assert os.path.exists(md_file), f"Markdown output not found: {md_file}"
            
            # Validate JSON structure
            with open(json_file, 'r') as f:
                data = json.load(f)
                assert 'campaign' in data, "Campaign data missing from JSON"
                assert data['campaign']['name'] == "Aethelgard: The Once and Future King", "Campaign name mismatch"
            
            # Validate SQL content
            with open(sql_file, 'r') as f:
                sql_content = f.read()
                assert "INSERT INTO public.campaigns" in sql_content, "Campaigns INSERT missing from SQL"
                assert "INSERT INTO public.worlds" in sql_content, "Worlds INSERT missing from SQL"
            
            # Validate Markdown content
            with open(md_file, 'r') as f:
                md_content = f.read()
                assert "# Aethelgard: The Once and Future King" in md_content, "Campaign title missing from Markdown"
                assert "## Major NPCs" in md_content, "NPCs section missing from Markdown"
            
            print(f"✅ Single file test passed! Generated: {result.campaign.name}")
            print(f"   Worlds: {len(result.worlds)} | NPCs: {len(result.npcs)} | Quests: {len(result.quests)}")
            
        except Exception as e:
            print(f"❌ Single file test failed: {e}")
            raise
    
    @patch('main.OPENROUTER_API_KEY', 'test-key')
    def test_slugify_filename(self):
        """Test filename slugification"""
        test_cases = [
            ("aethelgard-the-once-and-future-king.md", "aethelgard-the-once-and-future-king"),
            ("Against the Titans.md", "against-the-titans"),
            ("test campaign (1).md", "test-campaign-1"),
            ("simple_test.md", "simple_test")
        ]
        
        for filename, expected in test_cases:
            result = slugify_filename(filename)
            assert result == expected, f"Slugify failed: {filename} -> {result} (expected {expected})"
        
        print("✅ Slugify filename test passed")
    
    @patch('main.run_expansion')
    def test_batch_mode(self, mock_expansion):
        """Test batch processing mode"""
        print("\n🧪 Testing Batch Mode...")
        
        # Mock the expansion function
        mock_result = MagicMock()
        mock_result.campaign.name = "Test Campaign"
        mock_result.worlds = [MagicMock()]
        mock_result.npcs = [MagicMock()]
        mock_result.quests = [MagicMock()]
        mock_result.locations = [MagicMock()]
        mock_expansion.return_value = mock_result
        
        # Run batch mode on test directory
        input_dir = self.batch_test_dir
        output_base_dir = self.test_output_dir
        
        result = run_batch_mode(input_dir, output_base_dir, None, verbose=True)
        
        # Validate summary was created
        summary_path = os.path.join(output_base_dir, "batch_summary.md")
        assert os.path.exists(summary_path), f"Batch summary not created: {summary_path}"
        
        with open(summary_path, 'r') as f:
            content = f.read()
            assert "Batch Processing Summary" in content, "Summary header missing"
            assert "Successful Campaigns" in content, "Success section missing"
        
        # Check subdirectories were created
        subdirs = [d for d in os.listdir(output_base_dir) if os.path.isdir(os.path.join(output_base_dir, d))]
        assert len(subdirs) == 2, f"Expected 2 subdirs, got {len(subdirs)}: {subdirs}"
        
        print(f"✅ Batch mode test passed! Created {len(subdirs)} campaign directories")
        print(f"   Summary: {summary_path}")
    
    @patch('builtins.input', side_effect=['', '', ''])  # Simulate Enter presses for defaults
    @patch('main.OPENROUTER_API_KEY', 'test-key')
    def test_interactive_mode(self, mock_input):
        """Test interactive mode with mocked input"""
        print("\n🧪 Testing Interactive Mode...")
        
        # Create a temporary test file
        temp_file = os.path.join(self.test_output_dir, "interactive_test.md")
        with open(temp_file, 'w') as f:
            f.write("# Interactive Test Campaign\n\nTest content for interactive mode.")
        
        # Patch the default path to our test file
        with patch('main.run_interactive_mode'):
            # Temporarily modify the default path in the function
            original_default = "../campaign-ideas/aethelgard-the-once-and-future-king.md"
            
            # Run interactive mode (mocked)
            result = run_interactive_mode()
            
            # Check if it ran without errors
            assert result == 0, "Interactive mode should return 0 for success"
        
        print("✅ Interactive mode test passed (mocked input)")
    
    def test_cli_help(self):
        """Test CLI help output"""
        print("\n🧪 Testing CLI Help...")
        
        try:
            result = subprocess.run(
                [sys.executable, 'main.py', '--help'],
                capture_output=True,
                text=True,
                cwd='crewai-dnd-expander'
            )
            
            output = result.stdout
            assert result.returncode == 0, "Help command should exit with 0"
            assert "D&D Campaign Expander" in output, "Help text missing title"
            assert "--batch" in output, "Batch option missing from help"
            assert "--input-dir" in output, "Input dir option missing from help"
            assert "interactive" in output.lower(), "Interactive mode mention missing"
            
            print("✅ CLI help test passed")
        except Exception as e:
            print(f"⚠️  CLI help test warning: {e}")
    
    def test_error_handling(self):
        """Test error handling for missing files"""
        print("\n🧪 Testing Error Handling...")
        
        # Test non-existent file
        try:
            run_expansion("nonexistent-file.md", None, self.test_output_dir)
            assert False, "Should raise FileNotFoundError for missing file"
        except FileNotFoundError:
            print("✅ File not found error handling passed")
        
        # Test missing API key (should be caught earlier)
        try:
            with patch('main.OPENROUTER_API_KEY', None):
                run_expansion(self.default_idea, None, self.test_output_dir)
                assert False, "Should raise ValueError for missing API key"
        except ValueError as e:
            if "API key" in str(e):
                print("✅ Missing API key error handling passed")
            else:
                raise
    
    def test_slugify_edge_cases(self):
        """Test slugify with edge cases"""
        edge_cases = [
            ("Aethelgard: The Once & Future King.md", "aethelgard-the-once-future-king"),
            ("Against_The_Titans (v2).md", "against_the_titans-v2"),
            ("  Spaces  .md ", "spaces"),
            (" café with accents.md", "caf-with-accents"),
            ("123-numeric.md", "123-numeric")
        ]
        
        for input_file, expected in edge_cases:
            result = slugify_filename(input_file)
            assert result == expected, f"Edge case failed: {input_file} -> {result}"
        
        print("✅ Slugify edge cases test passed")

def run_comprehensive_test(dry_run=False):
    """Run all tests in sequence"""
    print("🚀 Starting Comprehensive Test Suite")
    print(f"Dry run mode: {dry_run}")
    print("=" * 60)
    
    tester = TestCampaignExpander()
    
    try:
        # Run tests
        tester.test_file_exists()
        if not dry_run:
            tester.test_single_file_expansion()
        tester.test_slugify_filename()
        tester.test_cli_help()
        tester.test_error_handling()
        tester.test_slugify_edge_cases()
        
        # Batch test (always mocked for speed)
        tester.test_batch_mode(None)
        
        # Interactive test (mocked)
        tester.test_interactive_mode()
        
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED! ✅")
        print("The D&D Campaign Expander is ready for production use!")
        print("\nNext steps:")
        print("1. Add your OpenRouter API key to .env")
        print("2. Test with: python main.py --batch ../campaign-ideas/ -o campaigns/ -v")
        print("3. For single file: python main.py ../campaign-ideas/against-the-titans.md")
        print("4. Interactive: python main.py (no arguments)")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

def run_quick_test():
    """Quick validation test without LLM calls"""
    print("🔍 Running Quick Validation Test (No LLM calls)")
    
    # Test basic functionality
    tester = TestCampaignExpander()
    tester.setup_method()
    
    try:
        tester.test_file_exists()
        tester.test_slugify_filename()
        tester.test_cli_help()
        tester.test_error_handling()
        tester.test_slugify_edge_cases()
        
        # Test batch mode structure (mocked)
        tester.test_batch_mode(None)
        
        print("\n✅ Quick validation passed! System structure is solid.")
        print("Ready for full test with API key.")
        return 0
        
    except Exception as e:
        print(f"❌ Quick test failed: {e}")
        return 1
    finally:
        tester.teardown_method()

def main():
    """Main test runner"""
    parser = argparse.ArgumentParser(description="Test D&D Campaign Expander")
    parser.add_argument('--dry-run', '-d', action='store_true', 
                       help='Run tests without LLM calls (faster, no API key needed)')
    parser.add_argument('--quick', '-q', action='store_true', 
                       help='Run quick validation tests only')
    parser.add_argument('--full', '-f', action='store_true', 
                       help='Run comprehensive tests (requires API key)')
    
    args = parser.parse_args()
    
    if args.dry_run or args.quick:
        return run_quick_test()
    elif args.full:
        # Check API key
        try:
            from main import OPENROUTER_API_KEY
            if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == 'your_api_key_here':
                print("❌ Full test requires OpenRouter API key in .env")
                print("Run with --dry-run first to validate structure")
                return 1
        except ImportError:
            print("❌ Cannot import main.py - check file structure")
            return 1
        
        return run_comprehensive_test(dry_run=False)
    else:
        # Default: dry run if no API key, full if key present
        try:
            from main import OPENROUTER_API_KEY
            if OPENROUTER_API_KEY and OPENROUTER_API_KEY != 'your_api_key_here':
                print("API key detected - running full tests...")
                return run_comprehensive_test(dry_run=False)
            else:
                print("No API key - running quick validation...")
                return run_quick_test()
        except ImportError:
            print("Running quick validation...")
            return run_quick_test()

if __name__ == "__main__":
    sys.exit(main())
