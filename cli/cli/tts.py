from TTS.api import TTS

class TTSSingleton:
    """Singleton class to load the text-to-speech model once and use it across requests."""

    _model: TTS | None = None

    def __new__(self, model_name: str | None):
        if self._model is None:
            self._model = TTS(model_name=model_name or "tts_models/en/ljspeech/fast_pitch").to("cuda")

        return self._model

