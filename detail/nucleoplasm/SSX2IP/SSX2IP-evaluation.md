---
type: protein-evaluation
gene: "SSX2IP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SSX2IP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SSX2IP / KIAA0923 |
| 蛋白名称 | Afadin- and alpha-actinin-binding protein |
| 蛋白大小 | 614 aa / 71.2 kDa |
| UniProt ID | Q9Y2D8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centriolar satellite, Centrosome, Basal body; 额外: Acrosome, ; UniProt: Cell junction, adherens junction; Nucleus; Cytoplasm, cytosk |
| 蛋白大小 | 10/10 | ×1 | 10 | 614 aa / 71.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052300, IPR021622; Pfam: PF11559 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite, Centrosome, Basal body; 额外: Acrosome, Equatorial segment, Principal piece | Supported |
| UniProt | Cell junction, adherens junction; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, c... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- adherens junction (GO:0005912)
- cell leading edge (GO:0031252)
- centriolar satellite (GO:0034451)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0923 |

**关键文献**:
1. SSX2IP: an emerging role in cancer.. *Biochemical and biophysical research communications*. PMID: 17904521
2. The conserved Wdr8-hMsd1/SSX2IP complex localises to the centrosome and ensures proper spindle length and orientation.. *Biochemical and biophysical research communications*. PMID: 26545777
3. SSX2IP promotes metastasis and chemotherapeutic resistance of hepatocellular carcinoma.. *Journal of translational medicine*. PMID: 23452395
4. The centriolar satellite protein SSX2IP promotes centrosome maturation.. *The Journal of cell biology*. PMID: 23816619
5. The novel centriolar satellite protein SSX2IP targets Cep290 to the ciliary transition zone.. *Molecular biology of the cell*. PMID: 24356449

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.6 |
| 高置信度残基 (pLDDT>90) 占比 | 34.9% |
| 置信残基 (pLDDT 70-90) 占比 | 16.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 51.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.6），有序残基占 51.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052300, IPR021622; Pfam: PF11559 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AFDN | 0.986 | 0.329 | — |
| ACTN1 | 0.937 | 0.335 | — |
| ACTN4 | 0.910 | 0.100 | — |
| WRAP73 | 0.905 | 0.743 | — |
| SSX2 | 0.864 | 0.329 | — |
| SSX3 | 0.832 | 0.096 | — |
| SSX2B | 0.815 | 0.000 | — |
| SSX4B | 0.808 | 0.000 | — |
| SSX4 | 0.806 | 0.000 | — |
| CCDC14 | 0.792 | 0.647 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:2215"(barcode fusion genetics two hybri | doi:10.15252/msb.20156660|pubm |
| ENSP00000340279.3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| YWHAQ | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| YWHAZ | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| IKBKG | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CCNH | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CDC42 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SSX2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12007189|imex:IM-20236| |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| NS | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.6 + PDB: 无 | pLDDT=68.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell junction, adherens junction; Nucleus; Cytopla / Centriolar satellite, Centrosome, Basal body; 额外:  | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SSX2IP — Afadin- and alpha-actinin-binding protein，非常新颖，仅有少数基础研究。
2. 蛋白大小614 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2D8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117155-SSX2IP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SSX2IP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2D8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
