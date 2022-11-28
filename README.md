# UI Widgets demos

**List of all currently available supervisely widgets:**

  - [1. Button](/001_button/README.md)
  - [2. Progress Bar](/002_progress_bar/README.md)
  - [3. Text](/003_text/README.md)
  - [4. Input](/004_input/README.md)
  - [5. Input Number](/005_input_number/README.md)
  - [6. Project Thumbnail](/006_project_thumbnail/README.md)
  - [7. Dataset Thumbnail](/007_dataset_thumbnail/README.md)
  - [8. Video Thumbnail](/008_video_thumbnail/README.md)
  - [9. Select](/009_select/README.md)
  - [10. Select Project](/010_select_project/README.md)
  - [11. Select Dataset](/011_select_dataset/README.md)
  - [12. Select Workspace](/012_select_workspace/README.md)
  - [13. Select Team](/013_select_team/README.md)
  - [14. Select Item](/014_select_item/README.md)
  - [15. Select TagMeta](/015_select_tag_meta/README.md)
  - [16. Checkbox](/016_checkbox/README.md)
  - [17. One of](/017_one_of/README.md)
  - [18. Notification Box](/018_notification_box/README.md)
  - [19. Done Label](/019_done_label/README.md)
  - [20. Object Class View](/020_object_class_view/README.md)
  - [21. Object Class List](/021_object_classes_list/README.md)
  - [22. Empty](/022_empty/README.md)
  - [23. Table](/023_table/README.md)
  - [24. Classic Table](/024_classic_table/README.md)
  - [25. Confusion Matrix](/025_confusion_matrix/README.md)
  - [26. Radio Table](/026_radio_table/README.md)
  - [27. Flexbox](/027_flexbox/README.md)
  - [28. Grid](/028_grid/README.md)
  - [29. Grid Gallery](/029_grid_gallery/README.md)
  - [30. Heatmap Chart](/030_heatmap_chart/README.md)
  - [31. Apex Chart](/031_apex_chart/README.md)
  - [32. Line Chart](/032_line_chart/README.md)
  - [33. Identity](/033_identity/README.md)
  - [34. Container](/034_container/README.md)
  - [35. Card](/035_card/README.md)
  - [36. Field](/036_field/README.md)
  - [37. Sidebar](/037_sidebar/README.md)
  - [38. Menu](/038_menu/README.md)
  - [39. Labeled Image](/039_labeled_image/README.md)
  - [40. Video](/040_video/README.md)

# How to debug widgets

**Step 1.** Prepare `~/supervisely.env` file with credentials. [Learn more here](https://developer.supervise.ly/getting-started/basics-of-authentication#how-to-use-in-python).

**Step 2.** Clone [repository](https://github.com/supervisely-ecosystem/ui-widgets-demos) with source code and create [Virtual Environment](https://docs.python.org/3/library/venv.html).

```bash
git clone https://github.com/supervisely-ecosystem/ui-widgets-demos
cd ui-widgets-demos
./create_venv.sh
```

**Step 3.** Open repository directory in Visual Studio Code

```bash
code -r .
```

**Step 4.** Open `.vscode/launch.json`

Select widget that you want to debug and enter its folder name to 10th line of `launch.json` as shown on an image below

![step_4](https://user-images.githubusercontent.com/48913536/202445858-0b381d46-d122-41c7-bb06-2fdf1a48b5e6.png)

**Step 5.** Launch widget app

To launch app with widget go to `Run and Debug` section and press `play` button as shown on an image below and go to uvicorn server specified in `launch.json` `0.0.0.0:8000`. Link to uvicorn server will be displayed in terminal.

![step_5](https://user-images.githubusercontent.com/48913536/202445868-12c35bae-f372-4a19-b01c-0b9e9ea38c0d.png)
