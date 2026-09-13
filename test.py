import argparse


def run_evaluation(data_root: str, checkpoint: str, report_dir: str) -> None:
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", required=True)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--report-dir", required=True)
    args = parser.parse_args()
    run_evaluation(args.data_root, args.checkpoint, args.report_dir)


if __name__ == "__main__":
    main()
