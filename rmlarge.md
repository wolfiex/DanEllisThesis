git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch model_diagnostics/figures_c3/mlpregressor/CVNOX_CapeVerde/O3.pdf' \
  --prune-empty --tag-name-filter cat -- --all
