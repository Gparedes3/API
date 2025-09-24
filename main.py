# main.py
from fastapi import FastAPI
from sqlmodel import select
from database import User, Product, create_all_tables, SessionDep

app = FastAPI()

# ------------------ EVENTO STARTUP ------------------
@app.on_event("startup")
def on_startup():
    # Crea las tablas al iniciar la app
    next(create_all_tables(app))

# ------------------ USERS CRUD ------------------

@app.post("/users/", response_model=User)
def create_user(user: User, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.get("/users/", response_model=list[User])
def read_users(session: SessionDep):
    return session.exec(select(User)).all()

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, session: SessionDep):
    return session.get(User, user_id)

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User, session: SessionDep):
    user = session.get(User, user_id)
    if user:
        user.name = updated_user.name
        user.email = updated_user.email
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
    return {"ok": True}

# ------------------ PRODUCTS CRUD ------------------

@app.post("/products/", response_model=Product)
def create_product(product: Product, session: SessionDep):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@app.get("/products/", response_model=list[Product])
def read_products(session: SessionDep):
    return session.exec(select(Product)).all()

@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, session: SessionDep):
    return session.get(Product, product_id)

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product, session: SessionDep):
    product = session.get(Product, product_id)
    if product:
        product.name = updated_product.name
        product.price = updated_product.price
        session.add(product)
        session.commit()
        session.refresh(product)
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, session: SessionDep):
    product = session.get(Product, product_id)
    if product:
        session.delete(product)
        session.commit()
    return {"ok": True}
