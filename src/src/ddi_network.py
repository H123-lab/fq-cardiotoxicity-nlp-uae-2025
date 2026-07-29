"""
===============================================================
Drug-Drug Interaction Network Analysis
===============================================================

Methods Section 2.14

Purpose

Characterize co-medication patterns
associated with fluoroquinolone
cardiotoxicity.

Outputs

• Interaction network
• Community detection
• Network visualization
"""

import networkx as nx


class DDINetwork:

    def __init__(self):

        self.graph = nx.Graph()

    def add_interaction(self,
                        drug_a,
                        drug_b):

        self.graph.add_edge(drug_a,
                            drug_b)

    def detect_communities(self):

        return list(
            nx.community.greedy_modularity_communities(
                self.graph
            )
        )

    def summary(self):

        return {
            "Nodes":
            self.graph.number_of_nodes(),

            "Edges":
            self.graph.number_of_edges()
        }


if __name__ == "__main__":
    print("DDI network initialized.")
