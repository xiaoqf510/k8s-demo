#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: $0 <action> <deployment> [namespace]"
    echo "Actions: undo, history"
    exit 1
fi

ACTION=$1
DEPLOYMENT=$2
NAMESPACE=${3:-default}

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
        exit 1
        ;;
esac

echo "Operation completed."
