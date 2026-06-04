---
type: protein-evaluation
gene: "MAD2L1BP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAD2L1BP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAD2L1BP / CMT2, KIAA0110 |
| 蛋白名称 | MAD2L1-binding protein |
| 蛋白大小 | 274 aa / 31.1 kDa |
| UniProt ID | Q15013 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Nuclear membrane; UniProt: Nucleus; Cytoplasm, cytoskeleton, spindle |
| 蛋白大小 | 10/10 | ×1 | 10 | 274 aa / 31.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=80.0; PDB: 2QYF, 6F0X |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009511, IPR053729; Pfam: PF06581 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Nuclear membrane | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear membrane (GO:0031965)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CMT2, KIAA0110 |

**关键文献**:
1. Multi-tiered chemical proteomic maps of tryptoline acrylamide-protein interactions in cancer cells.. *Nature chemistry*. PMID: 39138346
2. Biallelic MAD2L1BP (p31comet) mutation is associated with mosaic aneuploidy and juvenile granulosa cell tumors.. *JCI insight*. PMID: 37796616
3. Biallelic variants in MAD2L1BP (p31(comet)) cause female infertility characterized by oocyte maturation arrest.. *eLife*. PMID: 37334967
4. Lamina Associated Polypeptide 1 (LAP1) Interactome and Its Functional Features.. *Membranes*. PMID: 26784240
5. Linear ubiquitination of p31(comet) by HOIP couples cytokine response with mitotic regulation.. *Cell & bioscience*. PMID: 40462232

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.0 |
| 高置信度残基 (pLDDT>90) 占比 | 60.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.5% |
| 低置信 (pLDDT<50) 占比 | 17.2% |
| 有序区域 (pLDDT>70) 占比 | 69.3% |
| 可用 PDB 条目 | 2QYF, 6F0X |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2QYF, 6F0X）+ AlphaFold高质量预测（pLDDT=80.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009511, IPR053729; Pfam: PF06581 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC20 | 0.999 | 0.998 | — |
| TRIP13 | 0.997 | 0.977 | — |
| MAD2L1 | 0.996 | 0.988 | — |
| BUB1B | 0.834 | 0.625 | — |
| MAD1L1 | 0.827 | 0.611 | — |
| INPP5K | 0.735 | 0.616 | — |
| BUB3 | 0.625 | 0.000 | — |
| MAD2L2 | 0.521 | 0.230 | — |
| CENPI | 0.490 | 0.000 | — |
| CDC27 | 0.480 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP13 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| KRT15 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KAT5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| IGSF21 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.0 + PDB: 2QYF, 6F0X | pLDDT=80.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, spindle / Nucleoplasm, Nucleoli; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MAD2L1BP — MAD2L1-binding protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小274 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15013
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124688-MAD2L1BP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAD2L1BP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15013
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
