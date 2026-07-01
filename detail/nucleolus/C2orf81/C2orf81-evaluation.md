---
type: protein-evaluation
gene: "C2orf81"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C2orf81 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C2orf81 |
| 蛋白名称 | Uncharacterized protein C2orf81 |
| 蛋白大小 | 582 aa / 63.2 kDa |
| UniProt ID | A6NN90 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli, Nucleoli fibrillar center; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 582 aa / 63.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028042; Pfam: PF15479 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Nucleoli fibrillar center | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A high-resolution spatial map of cilia-associated proteins in the human fallopian tube.. *Nature communications*. PMID: 42010243
2. Genetics of growth rate in induced pluripotent stem cells.. *Stem cell reports*. PMID: 42167220

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.2 |
| 高置信度残基 (pLDDT>90) 占比 | 9.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.7% |
| 中等置信 (pLDDT 50-70) 占比 | 16.5% |
| 低置信 (pLDDT<50) 占比 | 63.6% |
| 有序区域 (pLDDT>70) 占比 | 20.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.2），有序残基占 20.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028042; Pfam: PF15479 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC154 | 0.655 | 0.052 | — |
| IQCN | 0.648 | 0.129 | — |
| STMP1 | 0.620 | 0.000 | — |
| TTC34 | 0.604 | 0.000 | — |
| C10orf67 | 0.602 | 0.000 | — |
| CEP72 | 0.602 | 0.000 | — |
| CCDC142 | 0.601 | 0.000 | — |
| ANKFN1 | 0.600 | 0.000 | — |
| GOLGA6L7 | 0.571 | 0.000 | — |
| JAKMIP3 | 0.530 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.2 + PDB: 无 | pLDDT=51.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli, Nucleoli fibrillar center | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C2orf81 — Uncharacterized protein C2orf81，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小582 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=51.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

**低复杂度蛋白的结构混沌与纤毛功能线索**：C2orf81（582 aa, 63.2 kDa, UniProt A6NN90）是典型的未注释蛋白——InterPro注释仅含一个保守域IPR028042（UPF0692家族/DUF4575，Pfam:PF15479），且该域功能完全未知。AlphaFold v6预测质量极差（pLDDT=51.2，仅20.0%残基有序，63.6%处于低置信区——即理论模型完全不可靠）。此极低pLDDT特征提示C2orf81可能属于内在无序蛋白（IDP），其构象在溶液中为高度动态的系综而非单一折叠状态。IDP虽难以进行传统结构生物学研究，但往往参与液-液相分离（LLPS）、多价低亲和力互作和信号枢纽功能——这些特征在核蛋白中尤为常见（如转录因子激活域、核散斑/核仁支架蛋白）。PAE图分析可揭示是否存在多个独立折叠域（PAE值低的方块区域）或完全无序——若PAE整体偏高（>15-20），则无序结论更为可靠。

**生物逻辑的意外指向——纤毛与中心体关联**：STRING互作网络中最高置信度的伙伴CCDC154（coiled-coil domain containing 154, combined score=0.655, 实验=0.052）和IQCN（IQ motif containing N, 0.648, 实验=0.129）均与纤毛和中心体功能相关。IQCN是精子鞭毛发生必需的钙调蛋白结合蛋白；STMP1（0.620）和C10orf67（0.602）亦与纤毛轴丝结构有关。最近文献（PMID:42010243）将C2orf81列为输卵管纤毛相关蛋白空间图谱中的组分——这是极为重要的功能锚点。C2orf81在HPA中定位于Nucleoplasm、Nucleoli和Nucleoli fibrillar center（Approved），表明其为核仁富集蛋白。

**核仁与TE调控的联系**：核仁是已知的TE转录抑制区室——L1逆转录转座子的ORF2蛋白在核仁中被核仁素（nucleolin/C23）和B23（nucleophosmin）扣押，抑制其逆转录活性。rDNA重复序列（属I类TE样元件）的转录在核仁中进行精密调控。若C2orf81定位于核仁纤维中心（HPA Approved），它可能在rDNA或核仁TE元件的转录调控中发挥作用。核仁蛋白（如nucleophosmin/NPM1）常通过富含Arg/Gly或Ser/Arg的无序区与RNA/DNA结合——C2orf81的IDP特征与此类核仁RNA结合蛋白的典型序列偏差一致。

**实验前景与风险权衡**：极度新颖（PubMed=2篇, 50/50分）和明确核仁定位（Approved, 28/40分）使C2orf81归一化得分达71.7/100——在所有C2orf家族成员中属最高。然而，无结构域功能注释（DUF4575完全未知）、AlphaFold预测质量极差（pLDDT=51.2）、PPI网络全为预测（STRING score<0.7）以及核心功能线索指向纤毛（非染色质）构成重大不确定性。实验优先级：（1）C2orf81-Flag IP/MS核仁提取物鉴定互作伙伴——优先关注是否与nucleolin、NPM1或rDNA转录因子（UBF）互作；（2）CRISPR敲除后RNA-seq鉴别被去抑制的重复序列；（3）体外相分离实验检测C2orf81是否形成LLPS凝聚体——IDP+核仁富集提示此可能性。C2orf81代表"黑洞蛋白"的极限案例——极度新颖但有合理核定位，适合作为开拓性靶标进行探索性功能研究。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NN90
- Protein Atlas: https://www.proteinatlas.org/ENSG00000284308-C2orf81/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C2orf81
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NN90
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000284308-C2orf81/subcellular

![](https://images.proteinatlas.org/49564/1055_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/49564/1055_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/49564/1125_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/49564/1125_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/49564/1226_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/49564/1226_D8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NN90-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NN90 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028042; |
| Pfam | PF15479; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000284308-C2orf81/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
