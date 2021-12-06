# Gram-Schmidt-Calculator

## What Is It?
A GUI calculator that can complete the Gram-Schmidt Process. The Gram-Schmidt process is a algorithm commonly used in linear algebra used for replacing a basis of a nonzero subspace of <img src="/eqs/rn.png"> with an orthogonal basis for that subspace.

## How Does It Work?

Before continuing, allow me to remind you of some elementary linear algebra terms. 

A **basis** is a set of linearly independent and nonzero vectors that represents a defined subspace.
**Orthogonal** is simply another term for perpendicular in a linear algebra sense. That is as much of a definition as you need for this explanation. 

Given a basis <img src="/eqs/x1p.png"> for a nonzero subspace *W* of <img src="/eqs/rn.png">, let:

<img src="/eqs/eq.png">

so that <img src="/eqs/v1p.png"> is an orthogonal basis for *W*.

## Calculator Capabilities
The calculator offers the following features:
- The ability to use any *m* x *n* matrix. 
- Short circuit feature if the basis is already an orthogonal basis. 
- GUI for easy use.

## Usage
1. Clone/download the repository. 
2. Run `main.py` with Python 3.

### Note: this application requires tkinter. 

Don't have it? No worries. Install it with:
```
pip install tk
```
