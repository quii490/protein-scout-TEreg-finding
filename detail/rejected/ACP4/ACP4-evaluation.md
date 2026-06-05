---
type: protein-evaluation
gene: ACP4
date: 2026-06-03
tags:
  - protein-evaluation
  - ACP4
  - nuclear-body
  - phosphatase
status: rejected
---

# ACP4 — 蛋白质评估报告

## 基本信息

| 属性 | 值 |
|------|-----|
| UniProt ID | Q9BZG2 |
| 蛋白质名称 | Testicular acid phosphatase |
| 别名 | ACPT |
| 氨基酸长度 | 426 aa |
| 分子量 | 46.1 kDa |
| AlphaFold 平均 pLDDT | 87.6 |
| pLDDT > 90 比例 | 73.7% |
| PubMed (strict) | 22 |
| PubMed (broad) | 38 |

## 核定位证据

### HPA 免疫荧光

- **主要定位**：Plasma membrane
- **附加定位**：Nuclear bodies, Microtubules
- **可靠性**：Approved
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA Approved级别免疫荧光将ACP4主要定位于质膜，同时检测到核体（Nuclear bodies）和微管的附加信号。Nuclear bodies是细胞核内的亚结构域（包括PML bodies、Cajal bodies等），提示该蛋白在特定条件下可能部分进入细胞核。但需要注意，其主要定位为质膜，核体仅为附加定位信号。

### UniProt 亚细胞定位

- **Membrane**（ECO:0000255，序列分析预测）

UniProt仅注释了Membrane定位，无核定位记录。ECO:0000255为基于序列分析的预测证据，非实验验证。

### GO-CC 细胞组分

| GO ID | 术语 | 证据 |
|-------|------|------|
| GO:0098978 | glutamatergic synapse | IEA:Ensembl（电子注释） |
| GO:0005764 | lysosome | IBA:GO_Central（生物学特征推断） |
| GO:0045211 | postsynaptic membrane | IBA:GO_Central（生物学特征推断） |

GO-CC完全未收录核定位相关术语。所有注释指向膜系统（溶酶体、突触后膜、谷氨酸能突触），与UniProt的Membrane注释一致。这一点与HPA的Nuclear bodies信号形成反差。

**核定位证据总结**：核定位证据强度较弱。HPA Approved IF在核体检测到信号，但仅为附加定位（非主要定位）。UniProt和GO-CC均未支持核定位，二者一致指向膜/溶酶体系统。该蛋白本质上是睾丸酸性磷酸酶，为膜相关蛋白，其核定位需要进一步实验验证。

## PubMed 文献证据

PubMed strict检索（标题/摘要含"ACP4" AND (gene OR protein OR hydrolase)）：22篇
PubMed broad检索（"ACP4"全文）：38篇

代表文献：

- **PMID: 36183038** — Liang T et al. (2022) "Enamel defects in Acp4(R110C/R110C) mice and human ACP4 mutations." *Scientific Reports*. 在小鼠模型中证实Acp4突变导致釉质发育缺陷，与人类ACP4突变所致釉质发育不全一致。
- **PMID: 34036831** — Kim YJ et al. (2022) "Recessive Mutations in ACP4 Cause Amelogenesis Imperfecta." *Journal of Dental Research*. 鉴定ACP4隐性突变导致遗传性釉质发育不全。
- **PMID: 37228816** — Bloch-Zupan A et al. (2023) "Amelogenesis imperfecta: Next-generation sequencing sheds light on Witkop's classification." *Frontiers in Physiology*. 利用NGS对釉质发育不全进行重新分类，ACP4为关键致病基因之一。
- **PMID: 15219672** — 最早报道ACP4可使ERBB4去磷酸化并抑制其配体诱导的蛋白水解切割。

文献主要集中在ACP4在牙齿发育（釉质形成）中的角色，少数涉及ERBB4信号调控。该基因已在牙齿发育领域建立明确的功能关联，但在核生物学方面的研究几乎空白。

## AlphaFold 结构 / PAE / PDB

- **AlphaFold条目**：AF-Q9BZG2-F1（version 6）
- **平均pLDDT**：87.6（高质量预测）
- **pLDDT分布**：>90: 73.7%, 70-90: 10.6%, 50-70: 7.5%, <50: 8.2%
- **PAE数据**：可用（pae_image_url、pae_doc_url均可得）
- **PDB结构**：无实验解析结构

AlphaFold预测整体质量良好，73.7%的残基pLDDT > 90。低于50的残基仅占8.2%，主要位于柔性区域。无PDB实验结构，但AlphaFold模型可用于初步结构分析和docking研究。

## InterPro / Pfam 结构域

| InterPro ID | Pfam ID | 描述 |
|-------------|---------|------|
| IPR033379 | - | Histidine acid phosphatase, active site |
| IPR000560 | PF00328 | Histidine phosphatase superfamily |
| IPR029033 | - | Histidine phosphatase superfamily |
| IPR050645 | - | Testicular acid phosphatase-like |

ACP4属于组氨酸磷酸酶超家族，含有特征性的组氨酸酸性磷酸酶活性位点。该结构域催化磷酸单酯水解，参与去磷酸化反应。从调控角度而言，酸性磷酸酶结构域主要执行催化功能而非转录调控或染色质重塑等经典核调控功能。

## STRING 蛋白互作网络

STRING数据库检索到15个功能伙伴（均为textmining来源，无实验验证互作）：

| 伙伴基因 | 综合得分 | 实验得分 | 数据库得分 | 文本挖掘 |
|----------|---------|---------|-----------|---------|
| ENAM | 0.716 | 0 | 0 | 0.716 |
| AMTN | 0.687 | 0 | 0 | 0.687 |
| KLK4 | 0.676 | 0 | 0 | 0.652 |
| AMBN | 0.674 | 0 | 0 | 0.671 |
| MMP20 | 0.532 | 0.071 | 0 | 0.512 |
| ODAPH | 0.620 | 0 | 0 | 0.620 |
| FAM20A | 0.596 | 0 | 0 | 0.587 |
| AMELX | 0.561 | 0 | 0 | 0.542 |
| WDR72 | 0.539 | 0 | 0 | 0.539 |
| ODAM | 0.535 | 0 | 0 | 0.535 |
| KLK1 | 0.514 | 0 | 0 | 0.514 |
| ACP7 | 0.513 | 0 | 0 | 0.500 |
| ACP5 | 0.480 | 0 | 0 | 0.473 |
| NDUFAB1 | 0.472 | 0 | 0.151 | 0.404 |
| RXFP4 | 0.468 | 0 | 0 | 0.457 |

值得注意的是，所有15个STRING伙伴均无实验互作证据（experimental=0），仅为文献共提及（textmining）。互作网络主要由釉质形成相关蛋白（ENAM, AMBN, AMELX, KLK4, MMP20, ODAPH, ODAM, AMTN，WDR72, FAM20A）组成，反映该蛋白在牙齿发育中的已知功能背景，而非物理互作网络。

## IntAct 分子互作

| 伙伴 | 检测方法 | PMID |
|------|---------|------|
| PPT | two hybrid array | 21798944 |
| ENST00000270593 | clash | 23622248 |

IntAct仅收录2条互作记录。PPT通过酵母双杂交阵列检测，为物理互作。另一条为未注释的转录本（ENST00000270593）通过CLASH方法检测。总体互作证据非常稀疏。

## 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA附加Nuclear bodies；主定位Plasma membrane |
| 蛋白大小 | 6/10 | ×1 | 6 | 426 aa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 |
| 三维结构 | 6/10 | ×3 | 18 | pLDDT 87.6；无PDB |
| 调控结构域 | 4/10 | ×2 | 8 | 组氨酸磷酸酶PF00328 |
| PPI网络 | 2/10 | ×3 | 6 | STRING textmining only |
| **加权总分** | | | **90/180** | |
| **归一化总分 (÷1.83)** | | | **49.2/100** | |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

## 最终决策

**Scored（低优先级，49.2/100）**

ACP4通过核评分阈值的初步筛选（nuclear_score=4 > 3），但全面评估显示其核定位证据强度有限。该蛋白本质为膜相关睾丸酸性磷酸酶，其主要功能在牙齿釉质形成中，亚细胞定位以质膜和溶酶体为主。HPA虽在核体（Nuclear bodies）检测到Approved级别的信号，但仅为附加定位，且UniProt、GO-CC均不支持核定位。

有利因素包括：适中的蛋白大小（426 aa）、较高质量的AlphaFold结构（mean pLDDT 87.6）、以及中等研究热度（PubMed=22，核生物学方向未开发）。不利因素主要为核定位证据薄弱（仅HPA附加定位）和PPI证据几乎为零（全部为textmining共提及）。综合得分15.85属于低分区间，建议在优先候选蛋白评估完成后再考虑该基因。

## Manual Review Note

ACP4作为睾丸酸性磷酸酶，传统认知为膜蛋白/分泌蛋白。HPA的Nuclear bodies信号可能反映：(1) 蛋白在生理条件下确实部分定位于核体，可能在特定核内过程中发挥未表征的非典型功能；(2) 抗体交叉反应或IF伪影，毕竟胞质/膜蛋白在固定后的染色有时会呈现核信号。鉴于GO-CC完全缺乏核术语、UniProt仅注释Membrane、且所有PPI证据均为textmining而非实验互作，保守判断其核定位可信度较低。如果后续能获得western blot核质分离或核定位序列预测的独立证据，可重新评估。目前建议以较低优先级保留在候选池中。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000142513-ACP4/subcellular

![](https://images.proteinatlas.org/48882/2048_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/48882/2048_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/48882/2118_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/48882/2118_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/48882/2180_C2_4_red_green.jpg)
![](https://images.proteinatlas.org/48882/2180_C2_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
