FROM ubuntu:20.04
ENV TZ=UTC
SHELL ["/bin/bash", "-c"]

# Actualiza y configura el entorno
RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    apt-get install -y tzdata apt-utils apt-transport-https curl wget  && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    apt-get upgrade -y

# Actualizamos los repos
RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y dotnet-sdk-6.0 aspnetcore-runtime-6.0 dotnet-runtime-6.0 

# Actualiza DoNete
RUN wget https://dot.net/v1/dotnet-install.sh && \
    chmod +x dotnet-install.sh && \
    ./dotnet-install.sh -c 6.0

# Instala bash y verifica su existencia
RUN apt-get install -y bash && \
    if [ ! -f /bin/bash ]; then echo "Bash not found!"; exit 1; fi && \
    ln -sf /bin/bash /bin/sh && \
    ls -l /bin/bash && ls -l /bin/sh

# Creamos el directorio y descargamos el runner
RUN mkdir actions-runner && cd actions-runner && \
    curl -o actions-runner-linux-x64-2.320.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.320.0/actions-runner-linux-x64-2.320.0.tar.gz && \
    tar xzf ./actions-runner-linux-x64-2.320.0.tar.gz

# Agrega el usuario y configura sudo
RUN useradd -m -s /bin/bash kaos && echo 'kaos:PASSWORD' | chpasswd && \
    usermod -aG sudo kaos && echo 'kaos ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    chown -R kaos:kaos /actions-runner && \
    chmod -R 755 /actions-runner

USER kaos
# Ejecuto la conexion con github
# esta parte hay que ejecutarla en el interior del docker (requeire respuestas) /actions-runner/config.sh --url https://github.com/SantaKa0S --token TOKEN
WORKDIR /home/kaos
CMD ["bash"]