# Installing memcached

```bash
sudo apt-get install memcached
```

## Configuring

### Sockets

If running the memcached on the same server as pinion.weather, it would be better to connect using sockets instead of a TCP connection

Sockets have a small advantage over TCP connections when it comes to speed

1. Edit the memcached config

   ```bash
   sudo nano /etc/memcached.conf
   ```

2. Comment out the line which listens for a TCP connection

3. Add the following lines

   ```bash
   # Set unix socket which we put in the folder /run/memcached
   -s /run/memcached/memcached.sock
   ```
   
4. Set the `config.ini` key `memcached` to `/run/memcached/memcached.sock`

5. Restart the memcached service