from concrete_creator import ConcreteCreator


def main() -> None:
    creator = ConcreteCreator()
    productA = creator.factory_method_a()
    productB = creator.factory_method_b()

    print(productA.operation_a() + " AND " + productB.operation_a())
    print(productA.operation_b() + " AND " + productB.operation_b())


if __name__ == "__main__":
    main()
