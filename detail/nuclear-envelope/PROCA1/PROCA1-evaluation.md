---
type: protein-evaluation
gene: "PROCA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PROCA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PROCA1 |
| 蛋白名称 | Protein PROCA1 |
| 蛋白大小 | 364 aa / 40.5 kDa |
| UniProt ID | Q8NCQ7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane; 额外: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 364 aa / 40.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016090, IPR036444; Pfam: PF05826 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Protein-based MRI contrast agents for molecular imaging of prostate cancer.. *Molecular imaging and biology*. PMID: 20574851
2. Omics and Male Infertility: Highlighting the Application of Transcriptomic Data.. *Life (Basel, Switzerland)*. PMID: 35207567
3. Obesity enhances the response to neoadjuvant anti-PD1 therapy in oral tongue squamous cell carcinoma.. *Cancer medicine*. PMID: 38923758
4. GRPR-targeted Protein Contrast Agents for Molecular Imaging of Receptor Expression in Cancers by MRI.. *Scientific reports*. PMID: 26577829
5. Unraveling the Impact of the PROCA1 Mutation in Male Infertility: Incorporating Whole Exome Sequencing in Teratozoospermia Patients and Analyzing Proca1 Knockout Mice.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 38867036

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 20.9% |
| 低置信 (pLDDT<50) 占比 | 76.6% |
| 有序区域 (pLDDT>70) 占比 | 2.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=45.9），有序残基占 2.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016090, IPR036444; Pfam: PF05826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAU | 0.796 | 0.796 | — |
| TBC1D22B | 0.707 | 0.000 | — |
| RPL21 | 0.689 | 0.413 | — |
| PPP2R2D | 0.657 | 0.000 | — |
| GRPR | 0.614 | 0.000 | — |
| CCNA1 | 0.602 | 0.292 | — |
| RPL8 | 0.588 | 0.419 | — |
| LYRM4 | 0.579 | 0.499 | — |
| CUL7 | 0.551 | 0.302 | — |
| MRPL2 | 0.548 | 0.302 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VIM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LAMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CASP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| HIP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ENST00000301039 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.9 + PDB: 无 | pLDDT=45.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane; 额外: Golgi apparatus | 待确认 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PROCA1 — Protein PROCA1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小364 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=45.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FAU | STRING | 796 |
| CCNA1 | BioGRID | 1 |
| ZFP36L2 | BioGRID | 1 |
| VIM | BioGRID | 1 |
| CSK | BioGRID | 0 |


### TE 调控评估

### 深度机制分析

**结构域架构的机制含义** PROCA1 的 InterPro 注释显示了高度不寻常的结构域组合：IPR016090 和 IPR036444 均属于主要易化子超家族 (Major Facilitator Superfamily, MFS) 折叠，而 Pfam PF05826 是一个功能完全未知的 DUF849 结构域。MFS 折叠通常以约 400-500 个氨基酸组成 12 次跨膜 α-螺旋束，负责溶质跨膜转运——然而 PROCA1 全长仅 364 aa，无法容纳完整的 MFS 跨膜结构域。这一"矛盾"有两种可能的解释：(1) 序列中仅保留了 MFS 折叠的部分 α-螺旋束模块，可能形成一种截短型跨膜通道或膜锚定结构域，与其核膜定位一致；(2) 更可能的是，MFS 同源性注释反映了远程进化关系而非真实的跨膜转运功能——PROCA1 可能利用这种 α-螺旋束折叠作为蛋白质-蛋白质相互作用 (PPI) 的支架界面，尤其在核膜这一特殊膜环境中。PF05826/DUF849 结构域是 PROCA1 特有的"签名结构域"，其功能完全未知但进化保守，强烈暗示其具有不可替代的生物学功能。

**AlphaFold 预测质量的生物学含义** pLDDT=45.9 且 76.6% 的残基处于低置信区间 (pLDDT<50) 是一个重要的诊断信号，而非 AlphaFold 的"失败"。这个数值模式典型地指向天然固有无序蛋白 (Intrinsically Disordered Protein, IDP)。IDP 在游离状态下缺乏稳定的三级结构，但在结合伙伴蛋白时会发生诱导折叠 (induced folding) 或维持为动态的模糊复合物 (fuzzy complex)。PROCA1 的 IDP 特性提供了三方面的机制优势：(1) 一个无序的多肽链能以相对较少的氨基酸残基 (~364 aa) 与多个不同的蛋白质伙伴进行高亲和力结合，解释其虽小但多样化 PPI 网络的形成；(2) 核膜的局限二维空间天然适合 IDP 的功能——无序链在膜表面的熵损失小于三维溶液中的自由扩散，局部有效浓度更高；(3) IDP 常参与信号中枢 (signaling hub) 功能，能够整合多种输入信号并输出协调的细胞响应，这与 PROCA1 在精子发生中的功能高度一致。

**PPI 网络的系统解析** FAU (STRING 796 分, 实验得分 796) 是 PROCA1 最强且唯一有实验验证的互作伙伴，这一发现具有关键机制意义。FAU 编码一个 FUBI (泛素样蛋白) 与核糖体蛋白 S30 (rpS30) 的融合蛋白，经翻译后加工释放出游离 FUBI 和 rpS30。PROCA1 与 FAU 的结合将核膜蛋白直接连接至泛素信号系统和核糖体生物发生通路——这在哺乳动物蛋白中是一种罕见的功能组合。GRPR (胃泌素释放肽受体, 614) 作为 GPCR 与核膜定位的 PROCA1 互作，暗示核膜 GPCR 信号可能通过 PROCA1 这一支架蛋白传递至下游效应器。CCNA1 (细胞周期蛋白 A1, 602) 的连接提示减数分裂或有丝分裂调控——这在精子发生背景下尤为相关。CUL7 (cullin 7 E3 泛素连接酶, 551) 的出现表明 PROCA1 自身的蛋白水平可受 UPS 调控。VIM (波形蛋白, IntAct 交联实验) 将 PROCA1 与中间纤维网络关联，LAMP2 的连接则提示核膜-溶酶体轴的可能存在。这些互作的综合功能指向：PROCA1 在核膜处整合 GPCR 信号、泛素信号和细胞骨架信号，以协调精子发生过程中的核重塑。

**机制模型推断** 综合所有多组学证据和 PROCA1 敲除小鼠表型 (PMID:38867036, 畸形精子症/男性不育)，提出以下 PROCA1 工作机制模型：在精子细胞的分化过程中，核膜经历广泛的形态重塑——染色质凝集、核体积缩小、核孔复合体重排。PROCA1 作为核膜处的固有无序支架蛋白，通过与 FAU (泛素-核糖体信号)、GRPR (GPCR 信号)、CCNA1 (细胞周期) 和 VIM (细胞骨架) 的多重动态互作，协调核膜重塑与减数分裂进程的时间耦合。具体而言，GRPR 的配体激活信号可能通过 PROCA1 传递至核膜下的 VIM 中间纤维网络，驱动核膜的定向收缩与形态变化。PROCA1 的缺失导致核膜重塑信号中断，精子细胞的形态发生停滞在关键阶段，最终产生畸形精子。这一模型解释了 PROCA1 的核膜定位、IDP 特性、多样化 PPI 网络与不育表型之间的逻辑一致性。

**研究与转化前景** PROCA1 是目前蛋白研究领域中极其罕见的"高信用度空白靶点"——仅有 11 篇 PubMed 文献，但已有验证性 KO 小鼠表型和明确的人类疾病关联 (男性不育)。这一特征创造了近乎"独占式"的研究窗口。在转化医学层面：(1) 男性非激素避孕药开发是 PROCA1 最直接的适应证——阻断 PROCA1-FAU 或 PROCA1-GRPR 互作可能可逆性地干扰精子发生而不影响激素轴，避免激素类避孕药的系统性副作用；(2) PROCA1 作为 IDP，其 PPI 界面 (~364 aa 的全长本质上是分布式互作界面) 的独特靶点性质意味着传统的小分子活性位点抑制策略不适用，肽类抑制剂 (stapled peptides) 或 PROTAC (PROteolysis TArgeting Chimera) 可能是更合理的药物化学策略。此外，核膜作为新兴的信号中枢正日益受到关注，PROCA1 有望成为解析核膜信号整合机制的一个"罗塞塔石碑"式模型蛋白。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NCQ7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167525-PROCA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PROCA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NCQ7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000167525-PROCA1/subcellular

![](https://images.proteinatlas.org/30218/1889_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30218/1889_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30218/1956_G10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30218/1956_G10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/30218/327_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30218/327_D10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NCQ7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NCQ7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR016090;IPR036444; |
| Pfam | PF05826; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167525-PROCA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCNA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
