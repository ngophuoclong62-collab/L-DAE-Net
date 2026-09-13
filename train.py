import argparse


def run_training(data_root: str, output_dir: str) -> None:
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    run_training(args.data_root, args.output_dir)


if __name__ == "__main__":
    main()
