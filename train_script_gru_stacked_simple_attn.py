from models import gru_stacked_simple
from helpers import checkpoint

# Get the review summary file
review_summary_file = 'extracted_data/review_summary.csv'

# Initialize Checkpointer to ensure checkpointing
checkpointer = checkpoint.Checkpointer('stackedSimple','gru','Attention')
checkpointer.steps_per_checkpoint(500)
checkpointer.steps_per_prediction(1000)
# Do using GRU cell - without attention mechanism
out_file = 'result/stacked_simple/gru/attention.csv'
checkpointer.set_result_location(out_file)
gru_net = gru_stacked_simple.NeuralNet(review_summary_file, checkpointer,attention=True)
gru_net.set_parameters(train_batch_size=5,test_batch_size=25, memory_dim=50,learning_rate=0.05)
gru_net.begin_session()
gru_net.form_model_graph(num_layers=2)
gru_net.fit()
gru_net.predict()
gru_net.store_test_predictions()
gru_net.close_session()
