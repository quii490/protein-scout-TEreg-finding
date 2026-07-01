---
type: protein-evaluation
gene: "C20orf27"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## C20orf27

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | C20orf27 |
| Protein Name | Adipose-secreted signaling protein |
| Size | 174 aa / 19.3 kDa |
| UniProt | Q9GZN8 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 174 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=3 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.1; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | ADISSP |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=32 |
| **加权总分** | | | **134.0/180** | |
| **归一化总分 (÷1.83)** | | | **73.2/100** | 互证: +1.0 |

### 3. Analysis
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=3, broad=4
- AF pLDDT: 80.1 / PDB: 0
- InterPro: ADISSP
- Pfam: DUF4517
- PPI degree=32 ChIP: None
36496438: A brown fat-enriched adipokine Adissp controls adipose thermogenesis and glucose | 40690096: C20orf27 promotes hepatocellular carcinoma progression via NT5E. | 32024300: C20orf27 Promotes Cell Growth and Proliferation of Colorectal Cancer via the TGF

### 4. Assessment
★★★★  **73.8/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Adipose-secreted signaling protein

**功能**: Adipocyte-secreted protein (adipokine) that acts as a key regulator for white adipose tissue (WAT) thermogenesis and glucose homeostasis at least in part through activation of protein kinase A (PKA)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026794 |
| Pfam | PF15006 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PHKB | BioGRID | 0 |
| RALYL | BioGRID | 0 |
| TERF2 | BioGRID | 0 |
| PPP1CC | BioGRID | 0 |
| PPP1CA | BioGRID | 0 |
| PPP1R3A | BioGRID | 0 |
| PPP1R7 | BioGRID | 0 |
| PPP1CB | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9GZN8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C20orf27

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000101220-C20orf27

![](https://images.proteinatlas.org/47483/766_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/47483/766_G12_3_red_green.jpg)
![](https://images.proteinatlas.org/47483/987_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/47483/987_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/47483/778_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/47483/778_G12_3_red_green.jpg)

### PubMed

**Count: 4**

| PMID | Title |
|---|---|
| 40876696 | C20orf27 regulates colorectal cancer growth and metastasis based on different lipid levels. |
| 40690096 | C20orf27 promotes hepatocellular carcinoma progression via NT5E. |
| 36496438 | A brown fat-enriched adipokine Adissp controls adipose thermogenesis and glucose homeostasis. |
| 32024300 | C20orf27 Promotes Cell Growth and Proliferation of Colorectal Cancer via the TGFβR-TAK1-NFĸB Pathway. |


### 深度机制分析

C20orf27 的域架构极为简约，含 174 个残基（19.3 kDa），由单个 ADISSP 结构域（IPR026794, Pfam PF15006/DUF4517）组成。ADISSP（脂肪细胞分泌的信号蛋白）结构域是一个功能定义但结构上仍未表征的模块，仅在一小组脊椎动物特异性分泌脂肪因子中保守。该蛋白缺乏任何经典信号传导或酶催化基序，甚至缺乏一个可识别的二级结构元素集合——预测表明富含环/转角的结构，带有一些 α-螺旋趋势，但缺乏明确的折叠拓扑。174 个残基中的如此构象简洁性在脂肪因子中并非罕见特征，它们通常将受体结合活性凝缩到一个小的、紧凑的结构域中，其折叠由二硫键维持。

结构表征处于中间状态（AlphaFold pLDDT=80.1），无实验 PDB 结构。尽管 pLDDT 较高，但若缺乏已知的同源折叠，仅有 pLDDT 且无实验验证，则预测结构的可靠性受限。根据 AF2 分析，该蛋白质由一个紧凑的 N 端核心（约残基 30-130，高 pLDDT）和 N 端与 C 端的柔性尾巴组成。pLDDT 曲线显示出 β-折叠和环形区域的清晰交替，提示该蛋白形成一个小的 β-三明治或 β-抓斗折叠。其胞外分泌蛋白的身份被普遍接受，但机制受体及该结构域的原子折叠仍属未知。

PPI 网络（degree=32, 主要为 BioGRID 低分连接）由一系列蛋白磷酸酶 1（PP1）调节亚基主导：PPP1CC、PPP1CA、PPP1R3A、PPP1R7 和 PPP1CB。这种 PP1 富集极其显著——PP1 全酶复合物由一个催化亚基和一个调节亚基组成，后者指导底物特异性和亚细胞定位。C20orf27 与多个 PP1 酶形式的互作表明它可能作为 PP1 的共同调节因子，整合脂肪因子信号以控制靶蛋白的去磷酸化率。PHKB（磷酸化酶 b 激酶调节亚基）的参与也支持其参与糖原代谢信号传导，这与 C20orf27 在棕色脂肪产热和葡萄糖稳态中的已知体内功能相吻合（PMID 36496438）。

核质和胞质双重定位（HPA Approved）提示 C20orf27 可能具有不依赖分泌的胞内角色。作为一种已确立的脂肪因子，它由脂肪细胞分泌并通过 PKA 激活对远处组织产生旁分泌/内分泌效应。然而，其胞内池可通过 TGFβR-TAK1-NFκB 通路（PMID 32024300）促进结直肠癌细胞生长和增殖。该蛋白还通过 NT5E（CD73，一种将胞外 AMP 转化为腺苷的胞外-5'-核苷酸酶）促进肝细胞癌（HCC）进展（PMID 40690096），从而提示了一种新的致癌途径：C20orf27 上调 CD73 依赖的腺苷生成，从而建立免疫抑制性肿瘤微环境。根据脂质水平的不同，其对 CRC 生长和转移的差异调控（PMID 40876696）表明，该蛋白可作为代谢物敏感信号节点发挥作用。

对 TE 调控而言，C20orf27 通过 TGFβR-TAK1-NFκB 轴的信号传导是一个有吸引力的切入点。NFκB 是许多内源性逆转录病毒 LTR 启动子（例如，来自 THE1/LTR10/MER41 家族的启动子）的主要转录因子。C20orf27-TAK1-NFκB 的激活可能驱动 TE 转录——特别是在炎性肿瘤微环境中。相反，C20orf27 的 PP1 调节功能可能使 NFκB 在 p65 亚基的 Ser536 位点或其他关键位点去磷酸化，从而作为 TE 激活的负反馈机制。脂肪因子信号传导、TE 去抑制和免疫监视之间的这种交叉点在高脂质条件下（如在肥胖相关癌症中）尤为引人注目。
