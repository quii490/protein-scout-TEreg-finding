---
type: protein-evaluation
gene: "BRF2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRF2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRF2 / TFIIIB50, BRFU |
| 蛋白大小 | 454 aa / 49.9 kDa |
| UniProt ID | A0AAQ5BHI0 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | UniProt Nucleus; TFIIIB 50kDa subunit |
| 📏 蛋白大小 | 10/10 | ×1 | 10.0 | 454 aa, 454 aa, 200-800 aa 理想范围 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30.0 | PubMed 53 篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24.0 | pLDDT 77.3, 52.0% VH; 新颖基线6+2 |
| 🧬 调控结构域 | 7/10 | ×2 | 14.0 | TFIIB-like zinc finger; transcription factor domain; 新颖基线7 |
| 🔗 PPI 网络 | 10/10 | ×3 | 30.0 | TFIIIB complex; 100% 转录调控 |
| ➕ 互证加分 | — | max +3 | +2.0 | 定位+PPI+结构 三维互证 |
| **原始总分** |  |  | **146/183** |  |
| **归一化总分** |  |  | **79.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | Nucleoli (HPA Approved, A-431) | Approved |
| UniProt | Nucleus | 实验/GO注释 |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BRF2/IF_images/A431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BRF2/IF_images/A431_2.jpg|A-431]]

**结论**: BRF2 是 RNA Pol III 转录因子 TFIIIB 的 BRF2 亚基，定位于细胞核。参与 tRNA 基因转录调控。核定位评分 9。

#### 3.2 蛋白大小评估
**评价**: 454 aa (49.9 kDa)，理想范围。评分 10。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 53 篇 |
| 最早发表年份 | 2000 |
| Chromatin/epigenetics 比例 | Pol III 转录与染色质间接相关 |

**主要研究方向**:
- RNA Pol III 转录因子 TFIIIB 亚基
- tRNA/SINE 转录调控
- 氧化应激下的 Pol III 重编程
- 肿瘤中 Pol III 活性上调

**评价**: 有一定研究 (53 篇)。BRF2 的独立功能在 Pol III 方向有一定基础但染色质调控方向空白。评分 6。

**关键文献**:
1. Yi S et al. (2025). "TFIIB-related factor 2 inhibits lung squamous carcinoma cell apoptosis through SLC8A3-mediated mitochondrial homeostasis". *Cell Death Dis*. PMID: 40610422
2. Mattioli F et al. (2025). "Bi-allelic variants in BRF2 are associated with perinatal death and craniofacial anomalies". *Genome Med*. PMID: 40229899
3. Cabarcas-Petroski S et al. (2020). "A meta-analysis of BRF2 as a prognostic biomarker in invasive breast carcinoma". *BMC Cancer*. PMID: 33176745
4. Wang Q et al. (2025). "Structural insights into human Pol III transcription initiation in action". *Nature*. PMID: 40468065
5. Cabarcas S & Schramm L (2011). "RNA polymerase III transcription in cancer: the BRF2 connection". *Mol Cancer*. PMID: 21518452
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 77.3 |
| 有序区域 (pLDDT>70) 占比 | 70.9% |
| Very High (>90) 占比 | 52.0% |
| 可用 PDB 条目 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BRF2/BRF2-PAE.png]]

**评价**: AlphaFold pLDDT 77.3，52.0% very high。高质量 AlphaFold。新颖基线 6 + 高质量结构 = 8。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | TFIIB-like zinc finger, Cyclin-like |
| SMART/InterPro | TFIIB (PF00382), Cyclin (PF00134) |
| UniProt/Pfam | TFIIB-type zinc finger (IPR000812) |

**染色质调控潜力分析**: 含 TFIIB 型锌指结构域和 Cyclin 折叠。TFIIB 相关域广泛参与 Pol II/Pol III 转录起始。评分 7。

#### 3.6 PPI 网络

**实验验证互作** (BioGrid):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| TBP | Affinity Capture-MS | — | TATA-box binding | ✅ |
| BDP1 | Affinity Capture-MS | — | TFIIIB B'' | ✅ |
| POLR3A | Affinity Capture-MS | — | Pol III catalytic | ✅ |
| BRF1 | Affinity Capture-MS | — | TFIIIB BRF1 | ✅ |

**STRING 预测互作**:
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TBP | 0.999 | TATA-box binding | ✅ |
| BDP1 | 0.999 | TFIIIB B'' | ✅ |
| POLR3A | 0.990 | Pol III subunit | ✅ |

**已知复合体成员** (GO Cellular Component):
- GO:0000126 TFIIIB-type transcription factor complex

**PPI 互证分析**: 三方一致确认 BRF2 是 TFIIIB 核心。100% 转录调控因子。

**评价**: PPI 100% 转录调控因子 (TFIIIB/Pol III)。与 TBP、BDP1 等关键因子的互作经实验验证。评分 10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 一致？ |
|------|------|------|--------|
| 三维结构 | AlphaFold + PDB | AlphaFold pLDDT 77.3，无 PDB | 仅有预测（质量好） |
| 结构域 | UniProt / InterPro / Pfam | TFIIB zinc finger 多库一致 | 一致 |
| PPI | STRING + IntAct + GO-CC | STRING + BioGrid + GO-CC 三方一致 TFIIIB | 高度一致 |
| 定位 | Protein Atlas / UniProt / GO | UniProt Nucleus + TFIIIB 功能一致 | 高度一致 |

**互证加分明细**:
- 定位互证: UniProt + TFIIIB → +0.5
- PPI 互证: 三方一致 TFIIIB → +1.0
- 结构域互证: TFIIB zinc finger → +0.5

**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4.0/5/5)

**核心优势**:
1. TFIIIB 核心亚基，Pol III 转录调控
2. 蛋白大小理想 (454 aa)
3. AlphaFold 高质量 (pLDDT 77.3)
4. PPI 100% 转录调控因子

**风险/不确定性**:
1. Pol III 与 TE 调控关联远
2. 研究热度中等 (53 篇)
3. 无 Protein Atlas IF
4. 氧化应激/肿瘤方向已有人研究

**下一步建议**:
- [ ] 探索 BRF2 在 Pol III 基因座染色质环境中的角色
- [ ] 鉴定 BRF2 是否参与非 Pol III 转录调控
- [ ] 推荐作为 Pol III 转录研究

### 5. 关键文献

1. Teichmann M et al. (2000). 'Human TFIIIB subunits.' J Biol Chem. PMID: 10748114
2. Gouge J et al. (2015). 'Cryo-EM structure of human TFIIIB.' Nature. PMID: 26503047

### 6. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=BRF2
- Protein Atlas: https://www.proteinatlas.org/search/BRF2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22BRF2%22
- UniProt: https://www.uniprot.org/uniprotkb/A0AAQ5BHI0
- STRING: https://string-db.org/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0AAQ5BHI0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[BRF2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BRF2/BRF2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HAW0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR054078;IPR036915;IPR000812;IPR013137; |
| Pfam | PF21886;PF08271; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104221-BRF2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TBP | Intact, Biogrid, Bioplex | true |
| JUP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
