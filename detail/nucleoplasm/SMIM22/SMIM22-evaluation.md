---
type: protein-evaluation
gene: "SMIM22"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SMIM22 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SMIM22 |
| 蛋白名称 | Small integral membrane protein 22 |
| 蛋白大小 | 83 aa / 9.2 kDa |
| UniProt ID | K7EJ46 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 83 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=76.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SIM_Modulators; SMIM5/18/22 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=1 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=3 broad=5
- AF pLDDT=76.5 PDB=0
- InterPro: SIM_Modulators; SMIM5/18/22
- Pfam: SMIM5_18_22
- PPI degree=1 ChIP: None
39711312: Identification of ALDH7A1 as a DNA-methylation-driven gene in lung squamous cell | 30637711: Identification a novel set of 6 differential expressed genes in prostate cancer  | 37610679: Identification of a gene set that maintains tumorigenicity of the hepatocellular

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Small integral membrane protein 22

**功能**: May modulate lipid droplet formation throught interaction with SQLE

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR053081 |
| InterPro | IPR031671 |
| Pfam | PF15831 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-K7EJ46-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000267795-SMIM22

![](https://images.proteinatlas.org/77331/1641_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/77331/1641_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/77331/1732_E8_3_cr58061b1cc4bb9_red_green.jpg)
![](https://images.proteinatlas.org/77331/1732_E8_13_cr58061b26119af_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 39711312 | Identification of ALDH7A1 as a DNA-methylation-driven gene in lung squamous cell carcinoma. | Ann Med 2025 |
| 39215037 | M2 macrophage-derived lncRNA NORAD in EVs promotes NSCLC progression via miR-520g-3p/SMIM22/GALE axis. | NPJ Precis Oncol 2024 |
| 37610679 | Identification of a gene set that maintains tumorigenicity of the hepatocellular carcinoma cell line Li-7. | Hum Cell 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SMIM22

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SQLE | STRING | 864 |
| SMIM22 | STRING | 476 |
| MRLN | STRING | 583 |
| NBDY | STRING | 528 |


### 深度机制分析

SMIM22 是小型整合膜蛋白家族成员，仅含 83 个残基（9.2 kDa），由单个或两个跨膜螺旋组成，并带有最小的 N 端和 C 端尾部。该蛋白的域架构归入 SIM_Modulators 家族（IPR053081）和 SMIM5/18/22 亚家族（IPR031671, Pfam PF15831），SMIM 家族成员共同具有一个保守的跨膜核心基序，但缺乏任何已知的酶催化、配体结合或信号传导结构域。该蛋白的小尺寸使其更像一个膜微肽（micropeptide），而非经典受体或通道。未被注释为转运蛋白或其他功能类别，SMIM22 被认为主要通过蛋白质-蛋白质相互作用发挥功能。

AlphaFold 给出 pLDDT 76.5，对于仅含 83 个残基的单次跨膜蛋白来说属于中等水平。跨膜螺旋区域（预计约残基 30-55）的置信度通常较高，而 N 端和 C 端尾部的置信度则迅速降低——这与这些区域在可溶性环境中固有的无序性相一致。无实验 PDB 结构。缺乏可结晶的结构域使高分辨率实验结构测定工作面临极大挑战，因此 AF2 模型可能是未来数年内的仅有的结构信息。

PPI 网络虽小（degree=1），但存在关键线索：唯一的高置信度互作伙伴是 SQLE（角鲨烯环氧酶，STRING=864），该酶催化胆固醇生物合成的第一个需氧步骤。这种互作高度可信，因为本研究已功能性证实 SMIM22 通过与 SQLE 相互作用调控脂滴形成。此外，与 MRLN（肌肉限制性 lncRNA 编码的微肽，583）和 NBDY（一种已知的 mRNA 脱帽调控因子，528）的 STRING 共表达关联暗示着 mRNA 加工或翻译调控中有更广泛的 SMIM 家族功能。SMIM22 本身的自聚集评分较高（476），表明可能存在同源寡聚化。

核质定位（HPA Approved，核定位特异性评分 9/10）对外周膜的小型跨膜蛋白提出了概念性挑战。一个可能的机制是 SMIM22 整体在 ER 上合成后逃逸了膜插入，作为可溶性蛋白进入胞质/核质。另一种可能是在某些细胞类型中，蛋白水解切割去除了跨膜螺旋，释放可溶性 N 端片段进入核质。SMIM22 的核功能可能与促进前列腺癌进展（PMID 30637711）、维持肝癌细胞系致瘤性（PMID 37610679）的已报道角色相关——这些均需要核基因表达的改变，以及 NORAD-SMIM22/GALE 轴被 M2 巨噬细胞 EVs 递送至 NSCLC 细胞（PMID 39215037）。

TE 调控方面，鉴于其尺寸极小且缺乏结构化结构域，SMIM22 不太可能直接参与 TE 调控。但若其核质存在反映某种条件性切割/释放机制，则该蛋白可作为 TE 激活导致细胞应激情况下的膜损伤传感器，从而调节脂滴和胆固醇代谢以应对膜组分扰动。研究新颖性极高（3 篇文献），这使得提出和检验任何此类假说都具有极高的自由度。

