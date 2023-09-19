FROM jlgingrich/disnake
# Copy in new extensions and remove the example one
COPY ./exts ./exts
# Install any additional requirements
RUN pip install -r requirements.txt