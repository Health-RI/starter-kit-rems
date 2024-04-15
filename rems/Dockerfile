FROM cscfi/rems:latest

# Install Python and pip
RUN apk add --no-cache python3 py3-pip
# Install authlib
RUN apk add --upgrade py3-authlib

# Set the working directory inside the container
WORKDIR /rems

# Copy configuration files into the container
COPY config.edn /rems/config/config.edn
COPY styles.css /rems/theme/styles.css
COPY theme.edn /rems/theme/theme.edn
COPY en.edn /rems/theme/extra-translations/en.edn
COPY logo_medium.png /rems/theme/public/img/logo_medium.png
COPY logo_small.png /rems/theme/public/img/logo_small.png
COPY ls_login.png /rems/theme/public/img/ls_login.png

# Copy the script to generate JWKS
COPY generate_jwks.py /rems

RUN python3 /rems/generate_jwks.py && \
    mkdir -p /rems/keys && \
    mv /rems/private-key.jwk /rems/keys/private-key.jwk && \
    mv /rems/public-key.jwk /rems/keys/public-key.jwk

# Expose the port the app runs on
EXPOSE 3000
