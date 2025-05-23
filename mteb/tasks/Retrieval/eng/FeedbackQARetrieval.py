from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class FeedbackQARetrieval(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="FeedbackQARetrieval",
        description="Using Interactive Feedback to Improve the Accuracy and Explainability of Question Answering Systems Post-Deployment",
        reference="https://arxiv.org/abs/2204.03025",
        dataset={
            "path": "lt2c/fqa",
            "revision": "1ee1cd0",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="precision_at_1",
        date=("2020-01-01", "2022-04-01"),
        domains=["Web", "Government", "Medical", "Written"],
        task_subtypes=["Question answering"],
        license="apache-2.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="created",
        bibtex_citation=r"""
@inproceedings{li-etal-2022-using,
  address = {Dublin, Ireland},
  author = {Li, Zichao  and
Sharma, Prakhar  and
Lu, Xing Han  and
Cheung, Jackie  and
Reddy, Siva},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
  doi = {10.18653/v1/2022.findings-acl.75},
  editor = {Muresan, Smaranda  and
Nakov, Preslav  and
Villavicencio, Aline},
  month = may,
  pages = {926--937},
  publisher = {Association for Computational Linguistics},
  title = {Using Interactive Feedback to Improve the Accuracy and Explainability of Question Answering Systems Post-Deployment},
  url = {https://aclanthology.org/2022.findings-acl.75},
  year = {2022},
}
""",
    )
