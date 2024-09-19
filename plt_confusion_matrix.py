labels_map = {i: str(i) for i in range(10)}


y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

if len(y_test.shape) > 1 and y_test.shape[1] != 1:
    y_test = np.argmax(y_test, axis=1)

y_test = np.vectorize(labels_map.get)(y_test)

y_pred_classes = np.vectorize(labels_map.get)(y_pred_classes)

labels = np.unique(np.concatenate((y_test, y_pred_classes)))

cm = confusion_matrix(y_test, y_pred_classes, labels=labels)
plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
