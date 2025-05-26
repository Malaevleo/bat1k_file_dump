install.packages('ape')
library(ape)
tree <- read.tree("bat_tags_upd.nwk")
is.rooted(tree)
root <- which(node.depth(tree) == max(node.depth(tree)))
print(root)
plot(tree, show.node.label = TRUE)
tree$tip.label
n_tips <- Ntip(tree)

# Determine if node 19 is a tip or internal node
if (19 <= n_tips) {
  cat("Node 19 is a tip with label:", tree$tip.label[19], "\n")
} else {
  # Internal node
  node_index <- 19
  internal_node_label <- tree$node.label[node_index - n_tips]
  cat("Node 19 is an internal node with label:", internal_node_label, "\n")
  
  # Find descendants of node 19
  descendants <- tree$edge[tree$edge[, 1] == node_index, 2]
  descendant_labels <- ifelse(descendants <= n_tips,
                              tree$tip.label[descendants],
                              paste("Node", descendants))
  cat("Descendants of Node 19:", descendant_labels, "\n")
}
# Highlight Node 19 with a red circle
plot(tree, show.node.label = TRUE)
tiplabels(pch = 19, col = "blue")  
nodelabels(bg = "red", frame = "circle", node = 19)  
