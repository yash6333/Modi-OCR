import os
from PIL import Image
from torch.utils.data import Dataset


class ModiCharacterDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        """
        root_dir:
            data/raw/MODI_HChar/MODI_HChar
        """
        self.root_dir = root_dir
        self.transform = transform
        self.samples = []
        self.class_to_idx = {}

        self._prepare_dataset()

    def _prepare_dataset(self):
        class_index = 0

        # consonants / digits / vowels
        for group in sorted(os.listdir(self.root_dir)):
            group_path = os.path.join(self.root_dir, group)
            if not os.path.isdir(group_path):
                continue

            # character folders (क, १, अ, etc.)
            for char in sorted(os.listdir(group_path)):
                char_path = os.path.join(group_path, char)
                if not os.path.isdir(char_path):
                    continue

                if char not in self.class_to_idx:
                    self.class_to_idx[char] = class_index
                    class_index += 1

                label = self.class_to_idx[char]

                for img_name in os.listdir(char_path):
                    img_path = os.path.join(char_path, img_name)
                    self.samples.append((img_path, label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        image = Image.open(img_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, label
