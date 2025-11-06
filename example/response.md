{
    "messages": [
        {
            "content": "What's the user's name?",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "human",
            "name": None,
            "id": "7b60bd10-482b-440b-b07a-fbb70f36b06f",
            "example": False,
        },
        {
            "content": "",
            "additional_kwargs": {
                "tool_calls": [
                    {
                        "id": "call_NLXqeaspNM98bR3ybrNLJxS2",
                        "function": {"arguments": "{}", "name": "get_user_data"},
                        "type": "function",
                    }
                ],
                "refusal": None,
            },
            "response_metadata": {
                "token_usage": {
                    "completion_tokens": 20,
                    "prompt_tokens": 198,
                    "total_tokens": 218,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-5-mini-2025-08-07",
                "system_fingerprint": None,
                "id": "chatcmpl-CL9QqiKrxiz6CevlekZXQWZZRJ18v",
                "service_tier": "default",
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            "type": "ai",
            "name": None,
            "id": "run--e70d4db3-0cb4-4aa4-bffe-7e7d225ce2aa-0",
            "example": False,
            "tool_calls": [
                {
                    "name": "get_user_data",
                    "args": {},
                    "id": "call_NLXqeaspNM98bR3ybrNLJxS2",
                    "type": "tool_call",
                }
            ],
            "invalid_tool_calls": [],
            "usage_metadata": {
                "input_tokens": 198,
                "output_tokens": 20,
                "total_tokens": 218,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        },
        {
            "content": '{"user_id": "kenny", "name": "Kenny"}',
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "tool",
            "name": "get_user_data",
            "id": "143f28b5-afa3-4df3-81b4-e0fbebd31b83",
            "tool_call_id": "call_NLXqeaspNM98bR3ybrNLJxS2",
            "artifact": None,
            "status": "success",
        },
        {
            "content": "The user's name is Kenny.",
            "additional_kwargs": {"refusal": None},
            "response_metadata": {
                "token_usage": {
                    "completion_tokens": 15,
                    "prompt_tokens": 239,
                    "total_tokens": 254,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-5-mini-2025-08-07",
                "system_fingerprint": None,
                "id": "chatcmpl-CL9QsD1YkmJLiJMaaJdxsz278Wt5o",
                "service_tier": "default",
                "finish_reason": "stop",
                "logprobs": None,
            },
            "type": "ai",
            "name": None,
            "id": "run--41c03b88-5238-420f-ac01-374d131571d9-0",
            "example": False,
            "tool_calls": [],
            "invalid_tool_calls": [],
            "usage_metadata": {
                "input_tokens": 239,
                "output_tokens": 15,
                "total_tokens": 254,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        },
    ]
}