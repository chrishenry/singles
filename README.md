# Sabermetrics

This repo relies on [Sean Lahman's Baseball Database](http://seanlahman.com/baseball-archive/statistics/). Download it and unzip into the `data` directory.

The recommended way to install and run this repo is using Docker.

The simplest way to install Docker is to install [the Platform from the official website](https://www.docker.com/products/docker). The official website offers [a good tutorial](https://docs.docker.com/engine/getstarted/).


# Batting stats

```bash
docker-compose run stats ./batting-stats.py
```
