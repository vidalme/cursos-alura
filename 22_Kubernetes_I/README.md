# Kubernetes: Pods, Services e ConfigMaps

1. Conhecendo o Kubernetes Ver primeiro vídeo
2. Criando o cluster
3. Criando e entendendo pods
4. Expondo pods com services
5. Aplicando services ao projeto
6. Definindo variáveis de ambiente


## 1. Conhecendo o Kubernetes Ver primeiro vídeo

![alt text](image-1.png)

Cluster, uma ou mais maquinas trablhando em um conjunto dividindo recursos.

![alt text](image.png)

![alt text](image-2.png)

![alt text](image-3.png)

## 2. Criando o cluster

hands on codigo

## 3. Criando e entendendo pods

![alt text](image-4.png)

- Pods são completamente efêmeros

``` shell
# cria pod com nginx inline (not normal)
kubectl run nginx-pod --image=nginx:latest

# observa em tempo real
kubectl get pods --watch

# display detalhes dos pods
kubectl describe pod nginx-pod

# edita pods
kubectl edit pod nginx-pod

# deleta um pod pelo nome
kubectl delete pod nginx-pod

# cria um pod definido em arquivo yaml
kubectl apply -f primeiro-pod.yaml 

# deleta o pod que foi definido nesse arquivo yaml
kubectl delete -f primeiro-pod.yaml 

#entra dentro do pod
kubectl exec -it portal-noticias -- bash

```
## 4. Expondo pods com services

![alt text](image-6.png)

![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-9.png)

![alt text](image-10.png)

![alt text](image-11.png)

![alt text](image-12.png)

5. Aplicando services ao projeto

hands on codigo

6. Definindo variáveis de ambiente

hands on codigo

![alt text](image-13.png)