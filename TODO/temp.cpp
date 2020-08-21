/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        // 递归,-1代替子树不平衡
        int res = helper(root);
        return res != -1;
    }
    int helper(TreeNode* root) {
        if(!root) return 0;
        int lh = helper(root->left);
        int rh = helper(root->right);
        if(rh == -1 || lh == -1 || abs(rh-lh) > 1) return -1;
        return max(rh, lh)+1;
    }
};