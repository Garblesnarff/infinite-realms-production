# Infinite Realms - Monitoring and Backup System

## Overview
This document describes the monitoring and backup infrastructure for the Infinite Realms production deployment on Hetzner server (91.98.173.12).

## System Architecture

### Components
- **API Service**: Node.js API running on PM2 (port 8888)
- **CrewAI Service**: Python CrewAI service on PM2
- **Supabase**: Self-hosted via Docker Compose (13 containers)
- **PostgreSQL**: Database on port 54321
- **Nginx**: Reverse proxy (not yet configured)

### Key Directories
- Application: `/var/www/infiniterealms/ai-adventure-scribe-main`
- Supabase: `/var/www/infiniterealms/supabase-docker/docker`
- Logs: `/var/log/infiniterealms/`
- Backups: `/var/backups/infiniterealms/postgres/`

## Monitoring

### Automated Monitoring
- **Script**: `/usr/local/bin/monitor-infiniterealms.sh`
- **Frequency**: Every 5 minutes via cron
- **Checks**:
  - API health endpoint (http://localhost:8888/health)
  - Supabase Docker containers status
  - PM2 process status
  - Database connectivity
  - Disk space usage (alerts at >90%)

### Log Files
- Status log: `/var/log/infiniterealms/status.txt`
- Alert log: `/var/log/infiniterealms/alerts.log`
- API logs: `/var/log/infiniterealms/api-out.log` and `api-error.log`
- Backup log: `/var/log/infiniterealms/backup.log`

### Manual Health Check
```bash
# Check all services
/usr/local/bin/monitor-infiniterealms.sh

# Check API health
curl http://localhost:8888/health

# Check PM2 processes
pm2 status

# Check Supabase containers
cd /var/www/infiniterealms/supabase-docker/docker
docker compose ps

# Check database
PGPASSWORD=Hs4rk7hs4rk7!1234 psql -h localhost -p 54321 -U postgres -d postgres -c "SELECT COUNT(*) FROM campaigns;"
```

## Backups

### Automated Backups
- **Script**: `/usr/local/bin/backup-infiniterealms-db.sh`
- **Schedule**: Daily at 2:00 AM UTC
- **Retention**: 7 days
- **Location**: `/var/backups/infiniterealms/postgres/`
- **Format**: Compressed SQL dumps (`.sql.gz`)

### Manual Backup
```bash
# Create backup now
/usr/local/bin/backup-infiniterealms-db.sh

# List all backups
ls -lh /var/backups/infiniterealms/postgres/
```

### Database Restore
```bash
# List available backups
/usr/local/bin/restore-infiniterealms-db.sh

# Restore from specific backup
/usr/local/bin/restore-infiniterealms-db.sh /var/backups/infiniterealms/postgres/infiniterealms_YYYYMMDD_HHMMSS.sql.gz
```

**WARNING**: Restore will:
1. Stop the API service
2. Drop and recreate the database
3. Restore from backup
4. Restart the API service

## Log Rotation

Application logs are automatically rotated using logrotate:
- **Configuration**: `/etc/logrotate.d/infiniterealms`
- **Frequency**: Daily
- **Retention**: 14 days
- **Compression**: Enabled (delayed by 1 day)

## Service Management

### Start/Stop Services
```bash
# API and CrewAI
pm2 start infinite-realms-api
pm2 stop infinite-realms-api
pm2 restart infinite-realms-api
pm2 logs infinite-realms-api

# Supabase
cd /var/www/infiniterealms/supabase-docker/docker
docker compose up -d      # Start all containers
docker compose stop       # Stop all containers
docker compose restart    # Restart all containers
docker compose logs db    # View database logs
```

## Database Information

- **Host**: localhost
- **Port**: 54321 (mapped from container port 5432)
- **Database**: postgres
- **User**: postgres
- **Password**: Hs4rk7hs4rk7!1234
- **Tables**: 47 total (23 Other, 7 Game, 6 Blog, 6 Character, 3 Combat, 2 Campaign)

### Key Tables
- `campaigns` - Game campaigns
- `characters` - Player characters with spells, inventory, stats
- `game_sessions` - Active game sessions
- `combat_encounters` - Combat system
- `inventory_items` - Item system
- `blog_posts` - CMS for blog content

## Troubleshooting

### API Not Responding
```bash
# Check PM2 status
pm2 status

# Check API logs
pm2 logs infinite-realms-api --lines 50

# Restart API
pm2 restart infinite-realms-api

# Check health
curl http://localhost:8888/health
```

### Database Connection Issues
```bash
# Test database connectivity
PGPASSWORD=Hs4rk7hs4rk7!1234 psql -h localhost -p 54321 -U postgres -d postgres -c "SELECT 1;"

# Check database container
cd /var/www/infiniterealms/supabase-docker/docker
docker compose ps db
docker compose logs db --tail 50

# Restart database
docker compose restart db
```

### Supabase Container Issues
```bash
cd /var/www/infiniterealms/supabase-docker/docker

# Check all containers
docker compose ps

# View logs for specific service
docker compose logs <service_name>

# Restart specific service
docker compose restart <service_name>

# Restart all Supabase services
docker compose restart
```

### Disk Space Issues
```bash
# Check disk usage
df -h

# Check backup directory size
du -sh /var/backups/infiniterealms/

# Clean old backups (older than 7 days)
find /var/backups/infiniterealms/postgres/ -name "*.sql.gz" -mtime +7 -delete

# Check Docker disk usage
docker system df

# Clean Docker cache
docker system prune -a
```

## Security Notes

1. Database password is stored in:
   - `/var/www/infiniterealms/ai-adventure-scribe-main/server/.env`
   - `/var/www/infiniterealms/supabase-docker/docker/.env`

2. Firewall (UFW) is configured to allow:
   - Port 22 (SSH)
   - Port 80 (HTTP)
   - Port 443 (HTTPS)

3. All services run as root (consider creating dedicated service user)

## Next Steps

1. **SSL Certificates**: Configure certbot for HTTPS
2. **Nginx Configuration**: Set up reverse proxy for API
3. **Domain Setup**: Configure infiniterealms.app DNS
4. **Remote Backups**: Set up off-site backup storage
5. **Monitoring Alerts**: Configure email/Slack notifications
6. **Security Hardening**: Create service user, restrict permissions
7. **Performance Monitoring**: Add Prometheus/Grafana or similar

## Support

For issues or questions:
- Check logs in `/var/log/infiniterealms/`
- Run monitoring script: `/usr/local/bin/monitor-infiniterealms.sh`
- Review this documentation
