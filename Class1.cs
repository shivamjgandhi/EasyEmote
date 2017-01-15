using System;
using Microsoft.ProjectOxford.Emotion;
using Microsoft.ProjectOxford.Emotion.Contract;

public class EmotionMaker
{
    public string[] Emotion(imageFilePath im)
    {

        EmotionServiceClient emotionServiceClient = new EmotionServiceClient(a5b5547007d54be7aa5bb75555376661);

        window.Log("Calling EmotionServiceClient.RecognizeAsync()...");
        try
        {
            Emotion[] emotionResult;
            using (Stream imageFileStream = File.OpenRead(im))
            {
                //
                // Detect the emotions in the URL
                //
                emotionResult = await emotionServiceClient.RecognizeAsync(imageFileStream);
                return emotionResult;
            }
        }
        catch (Exception exception)
        {
            window.Log(exception.ToString());
            return null;
        }
    }
}

namespace ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            EmotionMaker Emot;

            Emot = new EmotionMaker();
            var foo = Emot.Emotion("C: \\Users\\shivam gandhi\\Desktop\\download.jpg");
            Console.WriteLine(foo.Result);
            Console.ReadLine();
        }
    }
}
