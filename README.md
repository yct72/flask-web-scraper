# Simple Web Scraper
> Currently only for the Science topic of [National Geographic](https://www.natgeomedia.com/science/).
## Prerequisite
- MongoDB  
    For WSL2, both of the following work
    - [Install MongoDB - Microsoft Official Documentation](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-mongodb)  
    ** Noted that the service `mongodb` should be `mongod`
    - [Install MongoDB 4.4.1 on WSL 2 ](https://gist.github.com/matinrco/cdb3c0e5accc924b75c60b1648730867?permalink_comment_id=4459425#gistcomment-4459425)  

    If you encounter errors when starting mongod service, try
    - `rm /tmp/mongodb-27017.sock`  
        or  
    - `sudo chown mongodb:mongodb /var/run/mongod.pid`
- Python Packages
    - Requests  
    - Beautiful Soup  
    - Flask  
    - Pymongo

## Run
1. Start MongoDB
2. Run the script

    ```python
    python app.py
    ```
3. Open `http://127.0.0.1:9092`