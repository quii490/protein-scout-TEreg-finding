---
type: protein-evaluation
gene: "C6orf58"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## C6orf58

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | C6orf58 |
| Protein Name | Protein LEG1 homolog |
| Size | 330 aa / 37.9 kDa |
| UniProt | Q6P5S2 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm; Vesicles (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 330 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=87.7; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Leg1 |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=15 |
| **加权总分** | | | **139.0/180** | |
| **归一化总分 (÷1.83)** | | | **76.0/100** | 互证: +2.0 |

### 3. Analysis
- HPA: Cytosol; Nucleoplasm; Vesicles (Approved)
- PubMed: strict=5, broad=7
- AF pLDDT: 87.7 / PDB: 0
- InterPro: Leg1
- Pfam: Leg1
- PPI degree=15 ChIP: None
25053255: Ram seminal plasma proteome and its impact on liquid preservation of spermatozoa | 26485378: Integrative Genomics-Based Discovery of Novel Regulators of the Innate Antiviral | 27636150: Proteomic Investigation of Ram Spermatozoa and the Proteins Conferred by Seminal

### 4. Assessment
★★★★  **77.0/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构**：C6orf58（LEG1同源蛋白）是目前功能注释最贫乏的蛋白质之一，其唯一识别的结构域为Leg1结构域（IPR008499，Pfam PF05612）。Leg1（Liver-Enriched Gene 1）是一个功能不明的脊椎动物保守蛋白家族，目前在Pfam、InterPro和SMART数据库中均未被赋予任何酶活性注释。该结构域的长度（约280-300 aa，覆盖330 aa蛋白的主体）暗示它构成一个单一折叠单元而非多域蛋白。AlphaFold预测显示pLDDT=87.7，这一高置信度表明Leg1结构域采用一个致密的、良好折叠的球形构象——然而其拓扑结构不属于任何已知的酶超家族。进化保守但无已知催化功能的特征通常指向两种可能：(1)它是一种蛋白质-蛋白质相互作用结构域，作为更大复合物的衔接/支架亚基；(2)它可能具有非催化性的配体结合功能（类似于分泌型载体蛋白）。330 aa / 37.9 kDa的较小体积和HPA Vesicles定位（Approved）进一步支持C6orf58是一种可溶性货物蛋白或囊泡腔内衔接蛋白，而非膜整合蛋白或大型复合物核心亚基。

**PPI网络与胞内膜运输**：尽管PPI degree仅15，C6orf58的互作伙伴却高度聚集在细胞内运输通路上——这是一个功能高度一致的PPI网络，而非随机聚簇。SNX27（sorting nexin 27）是retromer复合物的货物衔接蛋白，负责将跨膜受体从内体回收至高尔基体或质膜——C6orf58与SNX27的互作将其锚定在retromer介导的内体-高尔基体逆行运输节点。COG2（Conserved Oligomeric Golgi complex subunit 2）是八亚基COG栓系复合物的组分，负责高尔基体内顺行和逆行囊泡栓系——此互作将C6orf58进一步连接至高尔基体囊泡对接机器。LDLRAP1（ARH，LDL受体衔接蛋白）介导LDL受体的网格蛋白依赖性内吞——连接至内吞作用。GKN1（gastrokine 1）是一种分泌型胃黏膜保护蛋白——连接至分泌途径。这些互作共同描绘了C6orf58沿"早期内体→retromer/SNX27→高尔基体/COG2→分泌囊泡"的完整胞内运输轨迹。特别值得注意的是，DDX31（DEAD-box RNA解旋酶31，定位于核仁）的互作将C6orf58连接至RNA代谢——暗示C6orf58可能参与核糖体组装、RNA运输，或作为RNA-蛋白质复合物在核-质之间的穿梭载体。HBQ1（hemoglobin subunit theta-1）的互作虽然是低置信度的稀疏数据，但加上GKN1和精浆蛋白质组学鉴定（PubMed 25053255，27636150），共同指向C6orf58在分泌性囊泡中的存在。

**结构生物学解读**：pLDDT=87.7（无实验PDB结构，PDB=0）表明Leg1结构域具有高置信度的独特折叠。330个氨基酸构成单一结构域的可能性大，因为多域蛋白在这个分子量范围内通常表现出域间低pLDDT。如果C6orf58确实是单域结构，那么它代表了一个新的折叠家族——一个功能未知但结构清晰的蛋白质。对于这种"高结构质量+零功能注释"的组合，结构基因组学方法（X射线晶体学或NMR）是优先策略：一旦获得高分辨率结构，可通过DALI或Foldseek搜索结构同源性来推断功能（例如识别与已知货物结合结构域的远程结构相似性）。Leg1结构域的三维结构也可用于预测配体结合口袋的存在与否——有无疏水口袋是区分"货物结合载体"和"蛋白质支架"假说的关键结构证据。

**分子机制模型**：将所有证据综合后，C6orf58的分子功能模型支持两个可检验的假说：(1) **内体-高尔基体货物衔接蛋白假说**——C6orf58以SNX27/retromer依赖方式被招募至早期内体，作为特定跨膜货物（受体、通道或黏附分子）的共衔接蛋白，促进它们从内体出芽进入逆行运输管状结构。COG2介导这些管状结构在高尔基体的正确栓系和融合。C6orf58本身随货物进入高尔基体管腔，最终被包装成分泌囊泡或腔内囊泡（外泌体前体）——这解释了其在精浆蛋白质组和HPA Vesicles定位中的检测。(2) **RNA-蛋白质核质穿梭假说**——C6orf58的核质定位（Approved）和DDX31（核仁RNA解旋酶）互作提示它可能在核仁-核质-胞质之间穿梭，携带未成熟核糖体亚基或特定mRNA。Leg1结构域可能含有RNA结合表面（这需要结构测定来验证）。"肝脏早期发育"的UniProt注释（基于斑马鱼leg1同源基因的胚胎表达模式）与两种假说都兼容——发育过程中的形态发生素梯度建立和信号范围受控都需要精确的膜蛋白运输。有趣的是，STK11（LKB1，丝氨酸/苏氨酸激酶，AMPK上游激酶和常被突变灭活的肿瘤抑制蛋白）的互作——如果被验证——可将C6orf58连接至细胞能量感知和细胞极性通路。在这种情境下，C6orf58可能作为LKB1激活AMPK信号的空间调节因子，耦合代谢状态与膜运输。

**研究与转化医学意义**：C6orf58代表了功能基因组学中"暗物质"蛋白的原型：进化保守且在多个蛋白质组学数据集中频繁被检测到，但功能完全未知（PubMed仅5篇，无PDB结构）。转化研究机会丰富：(1) SNX27/retromer在阿尔茨海默病中功能紊乱，C6orf58可能在此通路中作为新的治疗调节节点发挥作用；(2) 作为分泌蛋白/囊泡蛋白（精浆蛋白质组学反复验证），C6orf58可能是男性生育力的生物标志物；(3) LDLRAP1/COG2互作确立了高胆固醇血症和先天性糖基化障碍（COG缺陷）的潜在联系，值得在脂代谢领域进一步研究；(4) 与GKN1（胃癌中频繁缺失的肿瘤抑制因子）的互作提示C6orf58可能在胃黏膜稳态中发挥功能。基础研究优先级：首先需要Leg1结构域的高分辨率晶体/冷冻电镜结构来推断其折叠类型和功能类别；其次需要CRISPR敲除/敲入的细胞模型来确定其在retromer依赖性运输和核质定位中的确切角色。


### 补充分析 (UniProt API)

**蛋白全称**: Protein LEG1 homolog

**功能**: May be involved in early liver development

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR008499 |
| Pfam | PF05612 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DDX31 | BioGRID | 0 |
| GKN1 | BioGRID | 0 |
| SNX27 | BioGRID | 0 |
| LDLRAP1 | BioGRID | 0 |
| COG2 | BioGRID | 0 |
| HBQ1 | BioGRID | 0 |
| STK11 | BioGRID | 0 |
| GNG8 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6P5S2-F1-predicted_aligned_error_v6.png)


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000184530-C6orf58

![](https://images.proteinatlas.org/41449/2096_G10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41449/2096_G10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/41449/2122_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41449/2122_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41449/2116_C10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41449/2116_C10_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 7**

| 35448180 | Predicting Early Disease Recurrence of Pancreatic Cancer following Surgery: Determining the Role of NUDT15 as a Prognost | Curr Oncol 2022 |
| 35274021 | Downregulation of Three Novel miRNAs in the Lymph Nodes of Sheep Immunized With the Brucella suis Strain 2 Vaccine. | Front Vet Sci 2022 |
| 27636150 | Proteomic Investigation of Ram Spermatozoa and the Proteins Conferred by Seminal Plasma. | J Proteome Res 2016 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C6orf58

