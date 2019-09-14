# High or Low Card Game

As simple as time, try your best to guess whether the next card will be higher or lower!

### Now in a fun and interactive Docker container!

## Setup Process
---

### Build from source:
1. Clone this repository
   ```bash
   git clone https://github.com/clrosier/highcardlowcard.git && \
   cd highcardlowcard
   ```

2. Build the docker image
   ```bash
   sudo docker build -t highlow .
   ```

3. Run the docker image in interactive mode
   ```bash
   sudo docker run -i highlow
   ```

4. Play!

### Pull from dockerhub:
1. Pull the docker image from dockerhub
   ```bash
   sudo docker pull clrosier/highlow
   ```

2. Run the docker image in interactive mode
   ```bash
   sudo docker run -i clrosier/highlow
   ```

3. Play!