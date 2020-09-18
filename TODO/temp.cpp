    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        if(!root) return {};
		// 先序遍历
		st.push(root);
		while(st.size()) {
			TreeNode* tmp = st.top();
			res.push_back(tmp->val);
			st.pop();
			st.push(tmp->right);
			st.push(tmp->left);
		}
        return res;

    }