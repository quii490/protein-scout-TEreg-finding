---
type: protein-evaluation
gene: "ENTPD8"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## ENTPD8 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ENTPD8 |
| 蛋白名称 | Ectonucleoside triphosphate diphosphohydrolase 8 |
| 蛋白大小 | 495 aa / 53.9 kDa |
| UniProt ID | Q5MY95 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 495 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=11 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=94.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | GDA1_CD39_NTPase |
| PPI | 6/10 | x3 | 18.0 | PPI degree=66 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Vesicles (Approved)
- PubMed strict=11 broad=20
- AF pLDDT=94.4 PDB=0
- InterPro: GDA1_CD39_NTPase
- Pfam: GDA1_CD39
- PPI degree=66 ChIP: None
29987902: Identification of ENTPD8 and cytidine in pancreatic cancer by metabolomic and tr | 36130456: Identification of a 5-gene-based signature to predict prognosis and correlate im | 22266139: Next-generation sequencing identifies TGF-β1-associated gene expression profiles

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ectonucleoside triphosphate diphosphohydrolase 8

**功能**: Canalicular ectonucleoside NTPDase responsible for the main hepatic NTPDase activity (PubMed:17095758). Catalyzes the hydrolysis of nucleoside triphosphates (NTPs) and diphosphates (NDPs) (PubMed:16752921, PubMed:17095758, PubMed:17603550). The enzyme sequentially removes phosphate groups in two successive steps, converting NTPs to nucleoside monophosphates (NMPs) via NDP intermediates (PubMed:16752921, PubMed:17095758, PubMed:17603550). This activity contributes to the regulation of extracellul

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000407 |
| Pfam | PF01150 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CLEC2D | BioGRID | 0 |
| PBRM1 | BioGRID | 0 |
| SPPL3 | BioGRID | 0 |
| ENTPD2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5MY95-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000188833-ENTPD8

![](https://images.proteinatlas.org/21509/187_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/21509/187_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/21509/246_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/21509/246_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/21509/188_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/21509/188_B9_2_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能**：ENTPD8属于GDA1/CD39 NTPDase家族（InterPro: IPR000407; Pfam: PF01150），是外核苷三磷酸二磷酸水解酶（E-NTPDase）的8个成员之一。该家族标志性功能是二价阳离子依赖性地水解NTP和NDP，通过两步连续去磷酸化将NTP→NDP→NMP转化。ENTPD8是肝脏特异性的小管型NTPDase，主要负责肝细胞胆汁小管膜上的胞外核苷酸水解（PMID: 17095758, PMID: 16752921, PMID: 17603550）。其GDA1/CD39结构域采用保守的α/β折叠，包含五个apyrase保守区段（ACR1-5），共同构成磷酸结合口袋和金属离子配位位点。ENTPD8对UTP相较于ATP表现出底物偏好性，这在NTPDase家族中相对罕见，将ENTPD8定位于嘧啶能信号通路（而非嘌呤能P2受体通路）的关键调节位点。AlphaFold pLDDT=94.4是五个蛋白中最高水平之一，尽管尚无实验PDB结构（PDB=0），该高置信度模型已适用于计算辅助药物设计。

**PPI网络与核内功能线索**：ENTPD8的STRING PPI网络（degree=66）中，PBRM1（polybromo 1/BAF180, BioGRID count=0，源自高通量筛选）的潜在互作尤为引人深思。PBRM1是SWI/SNF（BAF/PBAF）染色质重塑复合物的核心亚基，含6个溴结构域、2个BAH结构域和一个HMG-box，专门识别乙酰化组蛋白并调节染色质可及性——PBRM1是透明细胞肾细胞癌中最频繁突变的染色质重塑因子之一。如果ENTPD8与PBRM1存在功能性互作，这为ENTPD8的核质定位提供直接机制：ENTPD8可能通过与PBAF染色质重塑机器的物理关联进入细胞核，或参与局部ATP/ADP浓度的调控以影响ATP依赖的SWI/SNF核小体滑动活性。ENTPD2（BioGRID count=0）作为同家族成员，可能通过异源寡聚化调节ENTPD8的酶活性或亚细胞靶向。SPPL3（信号肽肽酶样3）是Golgi驻留的膜内天冬氨酸蛋白酶，参与蛋白糖基化调控，与ENTPD8的潜在互作暗示蛋白水解加工在ENTPD8成熟或转运中的角色。

**结构解读**：pLDDT=94.4在495个氨基酸全长上代表了极高置信度，核心GDA1/CD39结构域几乎完全有序。GDA1/CD39折叠包含N端和C端两个结构相似的结构域，通过柔性铰链连接——在底物结合时发生闭合构象重排，将核苷酸底物夹在两个结构域之间进行催化。ACR保守序列区（ACR1-5）贡献关键催化残基：典型包括谷氨酸和天冬氨酸用于金属离子（Ca²⁺/Mg²⁺）配位，丝氨酸/苏氨酸用于磷酸基团过渡态稳定。ENTPD8对UTP的偏好性可能源于其底物结合裂隙中特异性识别尿嘧啶碱基的氢键网络——区别于识别腺嘌呤的ENTPD1/CD39或非选择性的ENTPD5。由于无实验结构（PDB=0），AlphaFold模型是目前唯一的高分辨率结构信息，缺乏核苷酸结合的holo构象是结构理解的显著缺口。

**分子机制模型**：ENTPD8的核质定位挑战了其仅作为肝细胞小管外核苷酸酶的经典认知。整合性模型提出ENTPD8在肝细胞内具有双重亚细胞定位：小管膜型负责胆汁核苷酸稳态，而核质型参与核ATP/GTP水平调控。核ATP不仅是SWI/SNF、ISWI、Mi-2/NuRD、INO80等所有染色质重塑复合物的必需底物，还是RNA聚合酶II转录延伸、DNA解旋酶活性和核小体滑动的直接能量来源。ENTPD8在核质中通过调节ATP/ADP/AMP比例可能间接调控这些核过程的动力学。另一种非互斥模型认为ENTPD8的核定位是一种调控储存形式——在肝细胞极性改变或肝损伤信号（如缺血-再灌注, PMID: 40600918）下从核内释放至小管膜，实现快速响应的核苷酸酶活性上调。TGF-β1信号通路与ENTPD8的表达关联（PMID: 22266139）支持了生长因子/应激信号调控ENTPD8定位和表达的观点。

**研究与治疗意义**：ENTPD8仅11篇严格PubMed文献（9/10新颖性），是五个评估蛋白中文献支持最少的一个。在肝脏缺血-再灌注损伤中NTPDase8的保护功能（PMID: 40600918）提示ENTPD8作为急性肝损伤治疗靶点的潜力——通过调控胞外ATP/UTP水平减轻无菌性炎症。整合转录组分析将其鉴定为胰腺癌代谢重编程和免疫微环境的预后基因标志物（PMID: 29987902, PMID: 36130456）及黑山羊肌肉品质调控因子（PMID: 40624004），显著拓展了其组织功能范围。核内定位的新发现为ENTPD8药物开发带来新的维度——针对其核内核苷酸酶功能的调控可能影响肝细胞染色质重塑活性，进而调控肝细胞分化、代谢和应激应答。利用高质量AlphaFold模型（pLDDT=94.4）进行虚拟筛选具有当下可行性，但长期仍需实验结构（X射线或冷冻电镜）捕获ENTPD8-核苷酸复合物的原子细节，为选择性抑制剂开发提供精确模板。

### PubMed 文献

**PubMed count: 20**

| 40624004 | Integrated transcriptomic analysis unveils molecular mechanisms regulating meat quality in newly improved black goat bre | NPJ Sci Food 2025 |
| 40600918 | NTPDase8 Protects Against Liver Ischemia-Reperfusion Injury in Mice. | FASEB J 2025 |
| 39997915 | Integrated Metabolomic and Transcriptomic Analysis Revealed the Mechanism of BHPF Exposure in Endometrium. | Toxics 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ENTPD8

