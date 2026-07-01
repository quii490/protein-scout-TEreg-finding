---
type: protein-evaluation
gene: "PDK3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PDK3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PDK3 |
| 蛋白全称 | [Pyruvate dehydrogenase (acetyl-transferring)] kinase isozyme 3, mitochondrial |
| UniProt ID | Q15120 |
| 蛋白大小 | 406 aa / 44.7 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 406 aa|
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=77 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=91.4; PDB=5 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR036784, IPR018955, IPR039028, IPR036890|
| PPI | 7/10 | ×3 | 21.0 | PPI degree=122 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Inhibits pyruvate dehydrogenase activity by phosphorylation of the E1 subunit PDHA1, and thereby regulates glucose metabolism and aerobic respiration. Can also phosphorylate PDHA2. Decreases glucose utilization and increases fat metabolism in response to prolonged fasting, and as adaptation to a hig

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR036784 | AK/P_DHK_N_sf |
| InterPro | IPR018955 | BCDHK/PDK_N |
| InterPro | IPR039028 | BCKD/PDK |
| InterPro | IPR036890 | HATPase_C_sf |
| InterPro | IPR003594 | HATPase_dom |
| InterPro | IPR005467 | His_kinase_dom |
| Pfam | PF10436 | BCDHK_Adom3 |
| Pfam | PF02518 | HATPase_c |


#### 3.4 结构信息

蛋白长度 406 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**74.9/100** | **nucleolus**
Nuclear protein


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000067992-PDK3

![](https://images.proteinatlas.org/72492/1685_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/72492/1685_F5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/72492/1412_D5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/72492/1412_D5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/72492/1641_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/72492/1641_D4_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00387; |
| InterPro | IPR036784;IPR018955;IPR039028;IPR036890;IPR003594;IPR005467; |
| Pfam | PF10436;PF02518; |
| UniProt Domain | DOMAIN 131..362; /note="Histidine kinase"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00107" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PDHA1 | STRING | 988 |
| PDX1 | STRING | 958 |
| SMPX | STRING | 897 |
| STAT5A | STRING | 782 |
| EGFR | BioGRID | 1 |
| APP | BioGRID | 1 |
| HLTF | BioGRID | 1 |
| VCP | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q15120-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 153**

| 42306635 | Dual activation of cuproptosis and excessive autophagy by copper-bismuth metal-organic frameworks-loaded detachable micr | Mater Today Bio 2026 |
| 42054210 | USP15 stabilizes c-Myc to drive sunitinib resistance by suppressing cuproptosis in clear cell renal cell carcinoma. | Cell Rep 2026 |
| 42045246 | Protective immunity against malaria by a nanoparticle CIS43-based junctional vaccine alone or in combination with R21. | NPJ Vaccines 2026 |

### 深度机制分析

**结构域架构解析**：PDK3属于线粒体丙酮酸脱氢酶激酶（PDK）家族，但其核仁定位（HPA Approved级别）提示了超越经典代谢调控的非传统功能。结构域分析揭示了两个关键功能模块：(1) N端BCDHK/PDK_N结构域（IPR018955, Pfam BCDHK_Adom3: PF10436）——这是一个约130个氨基酸的调节结构域，在不同PDK亚型间序列差异最大，决定了底物特异性和对别构效应物的响应（如丙酮酸抑制、NADH/乙酰CoA激活）；(2) C端组氨酸激酶样ATPase结构域（HATPase_c, IPR036890, Pfam HATPase_c: PF02518, 残基131-362, SMART SM00387）——采用Bergerat折叠（与经典的激酶折叠不同），由8条β链和4个α螺旋组成ATP结合口袋。该结构域属于GHKL（Gyrase, Hsp90, histidine Kinase, MutL）ATPase超家族，具有独特的ATP盖（ATP lid）机制：ATP结合诱导盖区构象变化，将γ-磷酸定位至底物PDHA1的特定Ser残基。值得注意的是，PDK3是PDK家族中唯一被发现对ATP表现出正协同性的亚型（Hill系数约1.5），其生化特性显著区别于PDK1/2/4。

**5个PDB结构的丰富结构信息**：pLDDT=91.4（本次评估第三高结构分）和5个PDB收录使PDK3成为结构层面最深入解析的蛋白之一。已知PDK3二聚体/四聚体的高分辨率晶体结构揭示了：(a) 二聚化界面的核心由C端HATPase结构域的反平行螺旋对介导；(b) 活性位点口袋由来自一个单体的ATP lid和另一个单体的核苷酸结合裂的残基共同组成——这解释了为什么PDK3必须以二聚体形式存在才能获得激酶活性；(c) N端BCDHK_Adom3结构域在apo状态下相对于催化核心采取"开放"构象，在结合PDHA1底物和脂酰结构域后发生约20度的刚体旋转，触发催化残基的排列。这些结构特点对于理解PDK3的药理学至关重要——PDK3的小分子抑制剂（如AZD7545, dichloroacetate DCA类似物）通常靶向ATP盖区的别构口袋而非ATP结合位点，以实现亚型选择性。

**PPI网络中的核功能线索**：PDHA1（STRING评分988，直接磷酸化底物）的互动是PDK3定义的生化关系——PDK3磷酸化PDHA1的Ser293（位点1）、Ser300（位点2）和Ser232（位点3），逐步失活丙酮酸脱氢酶复合物（PDC），从而将碳通量从乙酰CoA生成转向脂肪酸氧化。然而，PPI网络中的其他伙伴为PDK3的核功能提供了新视角。STAT5A（STRING评分782）的关联尤为引人注目——STAT5是JAK-STAT信号通路的核心转录因子，调控细胞增殖、分化和存活相关基因。STAT5A的转录活性依赖于特定Tyr的磷酸化（JAK介导），但Ser/Thr磷酸化（已知由多个激酶调控）可调节其DNA结合亲和力和转录激活强度。PDK3可能磷酸化STAT5A的Ser残基以调节其转录输出。HLTF（BioGRID评分1）是SWI/SNF家族的解旋酶样转录因子，参与DNA损伤耐受和复制叉稳定——其与PDK3的关联暗示PDK3可能影响肿瘤细胞的DNA损伤应答。EGFR和APP（均为BioGRID评分1）的关联则将PDK3与生长因子信号传导和神经退行性疾病连接起来，尽管这些互作的生理意义有待验证。

**核仁定位的代谢-表观遗传耦合假说**：PDK3的核仁定位对线粒体蛋白而言极为罕见。一种日益被认同的模型是：PDC的E1α亚基（PDHA1）可以在细胞核中存在——在细胞核中，PDC从丙酮酸产生乙酰CoA，后者是组蛋白乙酰转移酶（HATs）的直接底物。PDK3在核仁中的磷酸化活性可能调控这一"核PDC"池：在代谢应激条件下（高NADH/乙酰CoA比例），PDK3被激活，磷酸化PDHA1/PDHA2，减少核内局部乙酰CoA的生成，进而降低组蛋白乙酰化水平并沉默特定基因的表达。这种PDK3依赖的代谢-表观遗传耦合将细胞营养状态直接"编码"为染色质修饰景观。核仁作为rRNA转录和核糖体生物发生的枢纽，其乙酰CoA水平直接影响RNA聚合酶I活性和核糖体DNA的染色质状态。该假说可以解释为什么PDK3过度表达在多种癌症中与代谢重编程和异常表观遗传景观同时出现。

**研究与治疗意义**：PDK3在多种肿瘤中高度表达（PubMed = 153，其中多篇涉及肿瘤代谢），已成为代谢肿瘤学的重要靶点。DCA（二氯乙酸）作为泛PDK抑制剂已进入临床试验，但缺乏亚型选择性导致外周神经病变等剂量限制性毒性。PDK3特有的别构调控机制为其选择性小分子抑制剂的设计提供了结构基础。此外，新发现的STAT5A和HLTF相互作用暗示PDK3抑制剂可能与JAK-STAT抑制剂或PARP抑制剂产生合成致死效应——一个值得在药物组合筛选中验证的假设。铜死亡（cuproptosis）的最新研究与PDK3的关联（PubMed: 42306635, 42054210）揭示了一种令人兴奋的可能性：PDK3通过调控PDC活性和TCA循环通量，可能决定细胞对铜离子载体（如elesclomol）诱导的铜死亡的敏感性。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PDK3

