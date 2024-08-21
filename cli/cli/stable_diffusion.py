import torch
from diffusers import StableDiffusionPipeline, DiffusionPipeline

class StableDiffusionSingleton:
    """Singleton class to load the stable diffusion model once and use it across requests."""
    _model: DiffusionPipeline  | None = None

    def __new__(self):
        if self._model is None:
            self._model = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
            
        return self._model

