
from prompt_experimentation.run_local import LocalFlowExecution
from dotenv import load_dotenv

load_dotenv()


def main():
    data = "gcash_prompt_flow/data/data.jsonl"
    flow = "gcash_prompt_flow/flows/experiment"
    eval_flow = "gcash_prompt_flow/flows/evaluation"
    gcash_prompt_flow_flow = LocalFlowExecution(
        flow, eval_flow, data, {"url": "${data.url}"})
    gcash_prompt_flow_flow.process_local_flow()
    gcash_prompt_flow_flow.create_local_connections()
    run_ids = gcash_prompt_flow_flow.execute_experiment()

    gcash_prompt_flow_flow.execute_evaluation(run_ids, data, {
        "groundtruth": "${data.answer}",
        "prediction": "${run.outputs.category}"
    })


if __name__ == "__main__":
    main()
