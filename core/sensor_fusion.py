class SensorFusion:
    def fuse(self, data):
        if not data:
            return None

        total = 0
        for d in data:
            total += d.get("value", 0)

        return {
            "fused_value": total / len(data)
        }
