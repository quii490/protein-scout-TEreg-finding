---
type: protein-evaluation
gene: "NAF1"
date: 2026-06-04
tags: [protein-scout, confirmed-rejected, critical-false-rejection-recheck]
status: confirmed-rejected
previous_status: rejected
previous_rejection_reason: "nuclear_score ≤ 3 AND PubMed > 100 (dual rejection)"
recheck_result: "CONFIRMED REJECTED — PubMed 131>100(单独拒绝); HPA harvest失败; UniProt Cytoplasm+Nucleus(无实验证据代码); GO-CC空; 即使nuclear被修正, PubMed热度也会独立拒绝"
revised_nuclear_score: 3
note: "Harvest packet返回的UniProt条目Q15025为TNFAIP3-interacting protein 1(TNIP1/ABIN-1)，非telomerase NAF1。PubMed数据引用的是NAF1(telomerase)。存在gene symbol歧义。"
---

## NAF1 核蛋白评估报告 -- FALSE REJECTION RE-EVALUATION (确认拒绝)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAF1 (harvest返回TNFAIP3-interacting protein 1 / TNIP1) |
| 蛋白大小 | 636 aa / 70.0 kDa (harvest UniProt: Q15025) |
| UniProt ID | Q15025 (harvest返回) |
| 蛋白全名 | TNFAIP3-interacting protein 1 (harvest返回) / Nuclear assembly factor 1 (期望) |
| HPA IF 主定位 | (HPA查询失败: 'list' object has no attribute 'split') |
| HPA Reliability | (无) |
| 原评估状态 | REJECTED (nuclear_score=3, PubMed=131>100) |
| 重新评估日期 | 2026-06-04 |
| CONFIRMED REJECTED | **CONFIRMED REJECTED** — 双拒绝: (1)PubMed 131>100; (2)核定位数据不完整 |

### 2. 评分总览（修订后，确认原评分）

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | **3/10** | ×4 | 12 | HPA查询失败; UniProt Cytoplasm+Nucleus(无具体证据代码); GO-CC空 |
| 蛋白大小 | 8/10 | ×1 | 8 | 636aa/70.0kDa，中等大小 |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=131 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT=70.9; 无PDB实验结构 |
| 调控结构域 | 5/10 | ×2 | 10 | 无InterPro/Pfam注释(Harvest中); NF-kB通路调控功能 |
| PPI网络 | 4/10 | ×3 | 12 | STRING: DKC1/NOP10等(score=0); IntAct: 30个interactions(多为酵母) |
| **加权总分** | | | **60/180** | |
| **归一化总分 (÷1.8)** | | | **33.3/100** | |

### 3. False rejection recheck -- CRITICAL

**为何被列为CRITICAL进行重新评估:**

NAF1的PubMed 131篇超过100篇阈值，这是自动拒绝的独立原因。但核定位评分也是拒绝原因(nuclear_score=3)，因此需要确认: 如果仅考虑核定位，NAF1是否也是真正的非核蛋白? 还是双拒绝中的一个(PubMed)就已足够，无需关注核定位争论?

此外，harvest packet存在gene symbol歧义: harvest API对"NAF1"返回了Q15025 (TNFAIP3-interacting protein 1, 别名TNIP1/ABIN-1)，而非telomerase相关的NAF1 (Nuclear Assembly Factor 1)。但PubMed数据中引用的文献是关于telomerase NAF1(Dyskeratosis Congenita, telomere biology)。这表明存在gene symbol混淆，影响数据可靠性。

**Gene Symbol歧义说明:**

Harvest packet的UniProt记录:
- Accession: Q15025
- Protein: TNFAIP3-interacting protein 1 (TNIP1, ABIN-1)
- Function: Inhibits NF-kB, HIV-1 matrix interaction, regulates EGF-ERK signaling
- STRING partners: DKC1, NOP10, NHP2, GAR1等(telomerase/snoRNP复合物, 但score=0)

PubMed key papers引用的文献:
- "Dyskeratosis Congenita and Related Telomere Biology Disorders" — 这是关于telomerase NAF1的
- "Naf1 Regulates HIV-1 Latency by Suppressing Viral Promoter-Driven Gene Expression" — 可能也是telomerase NAF1

这种多义性意味着:
(1) Telomerase NAF1 (核蛋白，telomerase/snoRNP组装，H/ACA RNP复合物组分) — 可能是预期的目标
(2) TNIP1/ABIN-1 (TNFAIP3-interacting protein 1, NF-kB inhibitor) — harvest实际返回的

**逐一数据库审查 (使用harvest返回的Q15025/TNIP1数据):**

1. **UniProt Subcellular Location (harvest packet)**:
   - Cytoplasm: (无证据代码)
   - Nucleus: (无证据代码)
   - 两个定位但未提供证据等级 — harvest可能未解析证据代码字段

2. **GO-CC (harvest packet)**:
   - **空列表!** 完全无GO-CC注释

3. **HPA (harvest packet)**:
   - Error: "'list' object has no attribute 'split'" — HPA查询完全失败
   - 无任何HPA数据可用

4. **AlphaFold**:
   - 有结构预测 (pLDDT 70.9, 版本6)
   - 中等质量，32.7% pLDDT<50

5. **STRING**:
   - 所有伙伴score=0.0 (包括DKC1, NOP10, NHP2, GAR1等)
   - 这极不寻常 — 即使是co-expression也应该有非零score
   - 可能数据检索使用了不正确的标识符

6. **PubMed 131篇 — 单独拒绝**:
   - 无论gene symbol歧义如何解决，PubMed 131>100都会触发拒绝

**为何这不是假阴性:**

即使忽略gene symbol歧义和HPA/GO-CC数据缺失，NAF1也受到PubMed>100的独立拒绝。对于核定位而言:
- 如果TNIP1/ABIN-1: 已知的NF-kB抑制蛋白，有Cytoplasm和Nucleus双定位，但HPA数据缺失
- 如果telomerase NAF1: 明确的核仁蛋白(snoRNP组装)，但PubMed热度极高(>100)意味着已被广泛研究

无论哪种情况，NAF1/TNIP1都至少面临一个不可克服的拒绝原因。

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 | 备注 |
|------|------|--------|------|
| HPA (IF) | 无数据 | N/A | Harvest失败: 'list' object has no attribute 'split' |
| UniProt | Cytoplasm, Nucleus | 无证据代码 | Harvest未解析具体evidence等级 |
| GO-CC | (空) | N/A | 完全无注释 |

NAF1是10个CRITICAL基因中数据最不完整的。HPA查询失败、GO-CC空列表、UniProt证据代码缺失——三者同时发生意味着即使是基本的数据质量检查都无法通过。**核定位评分: 3/10 (鉴于数据缺失，无法给予更高或更低的评估)**。

#### 4.2 蛋白大小评估

636 aa / 70.0 kDa (Q15025/TNIP1)或493 aa (telomerase NAF1, 暂未验证)。中等大小。**评分: 8/10**。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 131 |
| 主要方向 | 先天性角化不良、telomere生物学、HIV潜伏、结直肠癌 

PubMed 131篇(>100)，自动REJECTED。该基因已被广泛研究。**评分: 0/10**。

**关键文献** (来自harvest PubMed数据):
1. "Dyskeratosis Congenita and Related Telomere Biology Disorders." PMID: 20301779
2. "Naf1 Regulates HIV-1 Latency by Suppressing Viral Promoter-Driven Gene Expression in Primary CD4+ T Cells." *J Virol*. PMID: 27795436
3. "Colorectal cancer-associated SNP rs17042479 is involved in the regulation of NAF1 promoter activity." *PLoS One*. PMID: 36067202
4. "Multiple splicing variants of Naf1/ABIN-1 transcripts and their alterations in hematopoietic tumors." *Int J Mol Med*. PMID: 17016622
5. "[Telomeres and lung]." *Rev Mal Respir*. PMID: 35715316

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 70.9 |
| pLDDT > 90 (Very High) | 39.3% |
| pLDDT < 50 (Low) | 32.7% |
| 有序区域 (pLDDT>70) | 56.6% |
| 实验结构 (PDB) | 无 |

AlphaFold中等质量，32.7%无序区域。无PDB实验结构。**评分: 6/10**。

#### 4.5 结构域分析

Harvest UniProt返回的interpro和pfam均为空列表。无结构域注释可用。如果为TNIP1/ABIN-1，已知含UBAN(ubiquitin binding in ABIN and NEMO)结构域和AHD1结构域; 如果为telomerase NAF1，含H/ACA RNP assembly domain。由于gene symbol歧义，暂不评估。**评分: 5/10**。

#### 4.6 PPI 网络

STRING所有伙伴score=0(包括DKC1/NOP10/NHP2/NOP58/FBL等telomerase/snoRNP复合物)。IntAct有30个interactions但数据格式混乱(多个酵母protein entries)。PPI数据异常可能反映标识符匹配错误。**评分: 4/10**。

### 5. 最终决定

**CONFIRMED REJECTED — PubMed 131>100导致自动拒绝，与原评估一致**

NAF1是10个CRITICAL基因中最具数据质量问题的案例:
1. **Gene symbol歧义**: Harvest返回TNIP1(Q15025)而非telomerase NAF1
2. **HPA查询失败**: 无任何HPA数据
3. **GO-CC缺失**: UniProt记录未包含任何GO-CC注释
4. **STRING异常**: 所有partner score=0
5. **PubMed 131>100**: 即使所有数据问题都解决，PubMed热度也会单独拒绝

**关于"false rejection"的结论**: 核定位评分=3在原评估中可能是基于不完整的数据，但即使将这个评分修正为5-6(如果telomerase NAF1有核仁定位)，PubMed 131>100仍然是拒绝的独立充分条件。因此，这不是一个false rejection——NAF1应保持拒绝状态，无论核定位证据如何。

**建议**: 如果未来需要评估telomerase NAF1，应使用正确的UniProt accession (Q96HR8, H/ACA ribonucleoprotein complex subunit NAF1)重新进行harvest。当前harvest返回的Q15025/TNIP1是不同基因。

### 6. 数据来源
- UniProt (harvest返回): https://www.uniprot.org/uniprotkb/Q15025 (TNIP1, 非telomerase NAF1)
- 期望的telomerase NAF1 UniProt: https://www.uniprot.org/uniprotkb/Q96HR8
- AlphaFold (Q15025): https://alphafold.ebi.ac.uk/entry/Q15025
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAF1%5BTitle/Abstract%5D
- HPA: 查询失败
- STRING: score异常(全0)
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/NAF1.json (2026-06-03)

所有图像均未下载。PAE未生成本地。
