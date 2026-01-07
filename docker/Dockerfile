FROM rm-docker

# Inject SSH public key into the VM
# Note: Key is passed as base64 to avoid shell escaping issues
ARG SSH_PUBLIC_KEY_B64
RUN set -ex && \
    if [ -n "$SSH_PUBLIC_KEY_B64" ]; then \
        echo "=== Decoding key ===" && \
        echo "$SSH_PUBLIC_KEY_B64" | base64 -d > /tmp/key.pub && \
        cat /tmp/key.pub && \
        echo "=== Starting VM ===" && \
        run_vm -serial null -daemonize && \
        wait_ssh && \
        echo "=== Creating .ssh directory ===" && \
        ssh -o StrictHostKeyChecking=no -o PasswordAuthentication=no root@localhost 'mkdir -p ~/.ssh && chmod 700 ~/.ssh && echo HOME=$HOME' && \
        echo "=== Injecting key ===" && \
        cat /tmp/key.pub | ssh -o StrictHostKeyChecking=no -o PasswordAuthentication=no root@localhost 'cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys' && \
        echo "=== Verifying key ===" && \
        ssh -o StrictHostKeyChecking=no -o PasswordAuthentication=no root@localhost 'cat ~/.ssh/authorized_keys' && \
        echo "=== Saving VM ===" && \
        save_vm && \
        rm /tmp/key.pub; \
    fi
