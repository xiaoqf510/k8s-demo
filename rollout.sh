#!/bin/bash

# 检查输入参数
if [ $# -lt 2 ]; then
    echo "Usage: $0 <action> <deployment> [namespace]"
    echo "Actions: undo, history"
    echo "Example: $0 undo jenkins-demo production"
    exit 1
fi

# 参数解析
ACTION=$1                # 操作类型，如 undo 或 history
DEPLOYMENT=$2            # 部署名称
NAMESPACE=${3:-default}  # 命名空间，默认为 default

# 执行操作
case $ACTION in
    undo)
        echo "Rolling back deployment $DEPLOYMENT in namespace $NAMESPACE..."
        kubectl rollout undo deployment "$DEPLOYMENT" -n "$NAMESPACE"
        ;;
    history)
        echo "Showing rollout history for deployment $DEPLOYMENT in namespace $NAMESPACE..."
        kubectl rollout history deployment "$DEPLOYMENT" -n "$NAMESPACE"
        ;;
    *)
        echo "Invalid action: $ACTION"
        echo "Valid actions: undo, history"
        exit 1
        ;;
esac

echo "Operation completed."
