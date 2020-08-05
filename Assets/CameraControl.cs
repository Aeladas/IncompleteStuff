using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraControl : MonoBehaviour
{
    [SerializeField] private int moveSpeed = 1;
    [SerializeField] private int rotateSpeed = 60;

    private void Update()
    {
        float x = Input.GetAxis("Horizontal") * Time.deltaTime * moveSpeed;
        float z = Input.GetAxis("Vertical") * Time.deltaTime * moveSpeed;
        float y = Input.GetAxis("Raise/Drop") * Time.deltaTime * moveSpeed;
        float ry = Input.GetAxis("Rotate Y") * Time.deltaTime * rotateSpeed;
        float rx = Input.GetAxis("Rotate X") * Time.deltaTime * rotateSpeed;

        gameObject.transform.Translate(x, y, z);
        gameObject.transform.Rotate(rx, ry, 0);
    }
}
