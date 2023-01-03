# Chatbot Backend


## ⚙️ Installation
```bash
docker run -p 8000:5000 ghcr.io/ibentau/chatbot-backend:main
```

The API will be available at http://localhost:8000

## 👩‍💻 How to use

### Get a response

```bash
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello"}' http://localhost:8000/
```
