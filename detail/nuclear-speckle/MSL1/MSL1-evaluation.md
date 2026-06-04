---
type: protein-evaluation
gene: "MSL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MSL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MSL1 / MSL1L1 |
| 蛋白名称 | Male-specific lethal 1 homolog |
| 蛋白大小 | 614 aa / 67.1 kDa |
| UniProt ID | Q68DK7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear speckles, Vesicles; UniProt: Nucleus; Nucleus, nucleoplasm; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 614 aa / 67.1 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=93 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.6; PDB: 4B7Y, 4B86, 4DNC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026711, IPR031840, IPR029332; Pfam: PF16801, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear speckles, Vesicles | Enhanced |
| UniProt | Nucleus; Nucleus, nucleoplasm; Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- MSL complex (GO:0072487)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 93 |
| PubMed broad count | 137 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MSL1L1 |

**关键文献**:
1. MSL1 Promotes Liver Regeneration by Driving Phase Separation of STAT3 and Histone H4 and Enhancing Their Acetylation.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37279389
2. Deciphering the binding between Nupr1 and MSL1 and their DNA-repairing activity.. *PloS one*. PMID: 24205110
3. N-terminus of Drosophila melanogaster MSL1 is critical for dosage compensation.. *eLife*. PMID: 39699942
4. Male-specific lethal 1 (MSL1) promotes Erastin-induced ferroptosis in colon cancer cells by regulating the KCTD12-SLC7A11 axis.. *Cell death & disease*. PMID: 40221412
5. Functional interplay between MSL1 and CDK7 controls RNA polymerase II Ser5 phosphorylation.. *Nature structural & molecular biology*. PMID: 27183194

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.6 |
| 高置信度残基 (pLDDT>90) 占比 | 13.7% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 55.7% |
| 有序区域 (pLDDT>70) 占比 | 27.2% |
| 可用 PDB 条目 | 4B7Y, 4B86, 4DNC |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.6），有序残基占 27.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026711, IPR031840, IPR029332; Pfam: PF16801, PF15275 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MSL2 | 0.999 | 0.950 | — |
| MSL3 | 0.999 | 0.985 | — |
| KAT8 | 0.995 | 0.934 | — |
| KAT5 | 0.956 | 0.493 | — |
| EP400 | 0.940 | 0.107 | — |
| MORF4L1 | 0.934 | 0.302 | — |
| BRD8 | 0.915 | 0.100 | — |
| ACTB | 0.910 | 0.103 | — |
| ACTL6A | 0.910 | 0.106 | — |
| EPC1 | 0.910 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cadps | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| CEP70 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| USHBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NINL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PSME3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRT15 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| AAR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| LEA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| BRR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| SMX3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.6 + PDB: 4B7Y, 4B86, 4DNC | pLDDT=57.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm; Nucleus speckle / Nucleoplasm; 额外: Nuclear speckles, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MSL1 — Male-specific lethal 1 homolog，研究基础较多，新颖性有限。
2. 蛋白大小614 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 93 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68DK7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188895-MSL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68DK7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
