import os
import sys
sys.path.append("../../../monk/");
import psutil

from gluon_prototype import prototype



gtf = prototype(verbose=1);
gtf.Prototype("sample-project-1", "sample-experiment-1");


gtf.Default(dataset_path="../../../monk/system_check_tests/datasets/dataset_cats_dogs_train", 
    			model_name="resnet18_v1", freeze_base_network=True, num_epochs=2);




###################################################   Dataset Updates    ######################################################################
gtf.update_input_size(256);
gtf.update_batch_size(6);
gtf.update_shuffle_data(True);
gtf.update_num_processors(psutil.cpu_count());
gtf.update_trainval_split(0.6);
gtf.update_dataset(dataset_path=["../../../monk/system_check_tests/datasets/dataset_cats_dogs_train", 
						"../../../monk/system_check_tests/datasets/dataset_cats_dogs_eval"]);
#################################################################################################################################################









###################################################   Transforms Updates    ######################################################################
# Reset Transforms if required
gtf.reset_transforms();
gtf.reset_transforms(test=True);
# Apply new transforms
gtf.apply_random_horizontal_flip(train=True, val=True);
gtf.apply_normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225], train=True, val=True, test=True);
#################################################################################################################################################


############################################ Auxiliary Functions - List all available transforms #########################################
gtf.List_Transforms()
######################################################################################################################################












#################################################   Model Updates ################################################################################
gtf.update_model_name("resnet50_v1");
gtf.update_use_gpu(True);
gtf.update_use_pretrained(True);
gtf.update_freeze_base_network(True);
gtf.update_freeze_layers(10);
#################################################################################################################################################


############################################ Auxiliary Functions - List all available models #########################################
gtf.List_Models();
######################################################################################################################################






#################################################   Apply additional layers to model ####################################################################
gtf.append_dropout(probability=0.1);
gtf.append_linear(final_layer=True);
######################################################################################################################################


############################################ Auxiliary Functions - List all available layers and activations #########################################
gtf.List_Layers();
gtf.List_Activations();
######################################################################################################################################







################################################# Training Param Updates ##########################################################################
gtf.update_num_epochs(5);
gtf.update_display_progress_realtime(False);    
gtf.update_display_progress(True);
gtf.update_save_intermediate_models(False); 
gtf.update_save_training_logs(True);
#################################################################################################################################################



###################################### Necessary Function to make model and datasetchanges as per updates ###########################################
gtf.Reload();
#################################################################################################################################################








################################################ Update Optimizer #########################################################################
gtf.optimizer_adam(0.001);
#################################################################################################################################################


############################################ Auxiliary Functions - List all available optimizers #########################################
gtf.List_Optimizers();
######################################################################################################################################







################################################ Update Learning rate schedulers #################################################################
gtf.lr_fixed();
#################################################################################################################################################


############################################ Auxiliary Functions - List all available schedulers #########################################
gtf.List_Schedulers();
######################################################################################################################################








################################################ Update Loss #################################################################
gtf.loss_softmax_crossentropy()
#################################################################################################################################################


############################################ Auxiliary Functions - List all available losses #########################################
gtf.List_Losses();
######################################################################################################################################






gtf.Train();




