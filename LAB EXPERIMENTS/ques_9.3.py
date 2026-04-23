# ===== Base Class =====
class A:
    def show_A(self):
        print("Class A (Base Class)")


# ===== Single Inheritance =====
class B(A):
    def show_B(self):
        print("Class B (Single Inheritance from A)")


# ===== Multilevel Inheritance =====
class C(B):
    def show_C(self):
        print("Class C (Multilevel Inheritance from B -> A)")


# ===== Hierarchical Inheritance =====
class D(A):
    def show_D(self):
        print("Class D (Hierarchical Inheritance from A)")


# ===== Multiple Inheritance =====
class E(B, D):
    def show_E(self):
        print("Class E (Multiple Inheritance from B and D)")


# ===== Hybrid Inheritance =====
class F(C, E):
    def show_F(self):
        print("Class F (Hybrid Inheritance)")


# ===== Main Program =====
obj = F()

print("\n--- Accessing Methods from All Classes ---")
obj.show_A()  # from A
obj.show_B()  # from B
obj.show_C()  # from C
obj.show_D()  # from D
obj.show_E()  # from E
obj.show_F()  # from F