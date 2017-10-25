from connexion.resolver import RestyResolver
import connexion

def main():
    print("Main")
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('AV_api.yaml', resolver=RestyResolver('api'))
    app.run(port="9090")

if __name__ == "__main__":
    print("All OK")
    main()