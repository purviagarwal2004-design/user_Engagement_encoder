import numpy as np

class EngagementEncoder:
    def __init__(self,total_users,total_features):
        self.total_users = total_users
        self.total_features = total_features
        self.user_feature_matrix = np.zeros((total_users, total_features), dtype=np.int32)

    def encode_engagement(self,user_id,feature_id):
        if user_id<0 or user_id>=self.total_users or feature_id<0 or feature_id>=self.total_features:
            raise ValueError("User ID or Feature ID is out of bounds.")
        self.user_feature_matrix[user_id][feature_id] = 1

    def log_activity(self,user_id,feature_id,count):
        if user_id<0 or user_id>=self.total_users or feature_id<0 or feature_id>=self.total_features:
            raise ValueError("User ID or Feature ID is out of bounds.")
        self.user_feature_matrix[user_id][feature_id] += count

    def total_actions(self):
        total_actions = np.sum(self.user_feature_matrix)
        user_engagements = np.count_nonzero(self.user_feature_matrix, axis=1)
        feature_engagements = np.count_nonzero(self.user_feature_matrix, axis=0)
        return total_actions, user_engagements, feature_engagements

if __name__ == "__main__":
    encoder = EngagementEncoder(total_users=5, total_features=3)
    encoder.encode_engagement(user_id=0, feature_id=1)
    encoder.log_activity(user_id=0, feature_id=1, count=2)
    encoder.encode_engagement(user_id=1, feature_id=2)
    encoder.log_activity(user_id=1, feature_id=2, count=3)

    total_actions, user_engagements, feature_engagements = encoder.total_actions()
    print("Total Actions:", total_actions)
    print("User Engagements:", user_engagements)
    print("Feature Engagements:", feature_engagements)
    
        
          