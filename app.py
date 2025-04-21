import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Function to apply Dijkstra's algorithm
def find_shortest_path(graph, source, target):
    # Dijkstra's algorithm to find shortest path
    path_length, path = nx.single_source_dijkstra(graph, source, target)
    return path, path_length

# Function to visualize the graph
def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    st.pyplot(plt)

# Streamlit user interface
def main():
    st.title("Shortest Path Problem Solver")
    
    # Create the graph from the given data
    graph = nx.Graph()

    # Define the towns (nodes)
    towns = ['A', 'B', 'C', 'D', 'E']
    
    # Define the distance (edges)
    distances = {
        ('A', 'B'): 10,
        ('A', 'C'): 50,
        ('A', 'D'): None,
        ('A', 'E'): None,
        ('B', 'C'): 20,
        ('B', 'D'): 55,
        ('B', 'E'): 40,
        ('C', 'D'): None,
        ('C', 'E'): 50,
        ('D', 'E'): 10
    }
    
    # Add edges to the graph with weights (distances)
    for (town1, town2), distance in distances.items():
        if distance is not None:
            graph.add_edge(town1, town2, weight=distance)

    # Display the graph
    st.subheader("Graph Representation")
    visualize_graph(graph)

    # User inputs for source and destination towns
    source = st.selectbox('Select the source town', towns)
    target = st.selectbox('Select the destination town', towns)

    # Button to solve the shortest path
    if st.button("Find Shortest Path"):
        if source != target:
            path, path_length = find_shortest_path(graph, source, target)
            st.subheader(f"Shortest Path from {source} to {target}")
            st.write(f"Path: {' -> '.join(path)}")
            st.write(f"Total Distance: {path_length} miles")
        else:
            st.write("Source and destination cannot be the same.")

if __name__ == "__main__":
    main()
